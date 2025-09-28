class ConfigException(Exception):
    """Base exception for configuration errors."""
    pass

class ConfigFileNotFoundException(ConfigException):
    """Exception raised when a configuration file is not found."""
    def __init__(self, filepath: str):
        self.filepath = filepath
        super().__init__(f"Configuration file not found: {self.filepath}")
