import re
from typing import Dict, Generator, List, Union


class TrtLogFile:
    """
    Core class for examining the TensorRT (TRT) log file.
    """

    def __init__(self, name: str, path: str) -> None:
        self.name = (name,)
        self.path = path

    def _parse_line(
        self, query: Union[None, list[re.Pattern]] = None
    ) -> Generator[str, Union[None, list[re.Pattern]], None]:
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

    def conversion_duration_info(self) -> List[Dict[str, float]]:
        """
        Extract conversion duration information for each stages of conversion.

        Returns:
        - List[Dict]: Information about each stage and duration (in seconds)
        """

        stages = [
            "Formats and tactics selection",
            "Engine generation",
            "Calibration",
            "Configuring builder",
            "Graph construction and optimization",
            "Finished engine building",
        ]
        re_stages_filter = [
            re.compile(rf"{pattern}.*?(\d+\.\d+)") for pattern in stages
        ]
        line_parser = self._parse_line(query=re_stages_filter)

        results = []
        for pr in line_parser:
            detected_stage = ""
            for s in stages:
                if s in pr:
                    detected_stage = s

            results.append(
                {
                    "stage": detected_stage,
                    "duration_s": float(re.findall(r"\d+\.\d+", pr)[0]),  # type: ignore
                }
            )

        return results
