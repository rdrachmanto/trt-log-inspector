class InvalidLogFileError(Exception):
    """Raised if log file is missing identities"""
    def __init__(self, missing: set, message="Log file is invalid, missing identities") -> None:
        self.message = message
        self.missing = missing
        super().__init__(f"{message}: {missing}")

