import logging

from config.models import LoggingConfig


def get_logger(config: LoggingConfig, logger_name: str) -> logging.Logger:
    """
    Create and configure a logger based on the provided configuration.

    :param logger_name: Name of the logger.
    :param config: LoggingConfig instance containing logging settings.
    :return: Configured logger instance.
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(config.level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(config.format)
    handler.setFormatter(formatter)
    if not logger.hasHandlers():
        logger.addHandler(handler)
    return logger
