from typing import List


class TrtLogFile:
    def __init__(self, name, path) -> None:
        self.name = name,
        self.path = path
        self.content = self._open_file_from_path()
    
    def _open_file_from_path(self) -> List[str]:
        """
        Open and read contents of the file from the provided path

        Args:
        - path (str): The relative path to the file

        Returns:
        - str: Contents of the file as str

        Raises:
        - FileNotFoundError: If the path specified is not accessible
        """
        try:
            with open(self.path) as f:
                contents = f.read()
            return contents.splitlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"{self.path} cannot be opened")

