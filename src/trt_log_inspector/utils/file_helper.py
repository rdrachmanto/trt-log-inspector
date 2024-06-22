def open_file_from_path(path: str) -> str:
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
        with open(path) as f:
            contents = f.read()
        return contents
    except FileNotFoundError:
        raise FileNotFoundError(f"{path} cannot be opened")

