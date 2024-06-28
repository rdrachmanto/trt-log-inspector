import re
from typing import Self, override
from collections.abc import Generator

from prettytable import PrettyTable
import pandas as pd  # type: ignore[reportMissingStubs]
import matplotlib.pyplot as plt

from trt_log_inspector.coreutils.display_log_data import DisplayLogData
from trt_log_inspector.coreutils.validations import InvalidLogFileError


class TrtLogFile(DisplayLogData):
    """
    Core class for examining the TensorRT (TRT) log file.
    """

    def __init__(self, name: str, path: str) -> None:
        self.name: str = name
        self.path: str = path
        self.results: list[dict[str, object]] = []

        self._check_trt_log_validity()

    def _parse_line(
        self, query: None | list[re.Pattern[str]] = None
    ) -> Generator[str, None | list[re.Pattern[str]], None]:
        """
        Attempt to open the file from `self.path` and apply query (if specified) to filter the text.

        Args:
        - query: compiled regex pattern to match against.

        Yields:
        - str: A stripped line from the file that matched the query.

        Raises:
        - FileNotFoundError: If file from self.path does not exist.
        """

        try:
            with open(self.path) as f:
                for line in f:
                    if query is not None and any(p.search(line) for p in query):
                        yield line.strip()
                    elif query is None:
                        yield line.strip()
        except FileNotFoundError:
            raise FileNotFoundError(f"{self.path} cannot be opened")

    def _check_trt_log_validity(self) -> None:
        """
        Checking validity of log file by matching against some information:
        - Input filename
        - ONNX IR version
        - Opset version
        - Producer name
        - Producer version

        Raises:
        - InvalidLogFileError: If any information is missing in the log file.
        """

        identities = [
            "Input filename",
            "ONNX IR version",
            "Opset version",
            "Producer name",
            "Producer version",
        ]
        re_ident_filter = [re.compile(f"{pattern}.*") for pattern in identities]
        line_parser = self._parse_line(query=re_ident_filter)

        matches: set[str] = set()
        for pr in line_parser:
            for id in identities:
                if id in pr:
                    matches.add(id)

        missing = set(identities) - matches
        if missing:
            raise InvalidLogFileError(missing)

    def conversion_duration_info(self) -> Self:
        """
        Extract conversion duration information for each stages of conversion.

        Returns:
        - List[Dict]: Information about each stage and duration (in seconds)
        """

        stages = [
            "Formats and tactics selection",
            "Engine generation",
            "Calibration",
            "Post Processing Calibration",
            "Configuring builder",
            "Graph construction and optimization",
            "Finished engine building",
        ]
        re_stages_filter = [
            re.compile(rf"{pattern}.*?(\d+\.\d+)") for pattern in stages
        ]
        line_parser = self._parse_line(query=re_stages_filter)

        for pr in line_parser:
            detected_stage = ""
            for s in stages:
                if s in pr:
                    detected_stage = s

            self.results.append(
                {
                    "stage": detected_stage,
                    "duration_s": float(re.findall(r"\d+\.\d+", pr)[0]),  # type: ignore[reportAny]
                }
            )

        return self

    @override
    def display_table(self) -> None:
        table = PrettyTable()
        table.field_names = list(self.results[0].keys())
        table.align = "l"

        for r in self.results:
            table.add_row(list(r.values()))  # type: ignore[reportUnknownMemberType]

        print(table)

    @override
    def display_plot(self):
        rec = pd.DataFrame.from_records(self.results)  # type:ignore[reportUnknownMemberType]

        rec.plot(x="stage", y="duration_s", kind="bar")  # type:ignore[reportUnknownMemberType]
        plt.tight_layout()
        plt.grid()  # type:ignore[reportUnknownMemberType]
        plt.show()  # type:ignore[reportUnknownMemberType]
