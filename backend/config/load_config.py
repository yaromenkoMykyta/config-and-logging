from __future__ import annotations
import os
import yaml
from pydantic import ValidationError

from config.models import BaseConfig
from config.exceptions import ConfigFileNotFoundException, ConfigException

_DEFAULT_CONFIG_PATHS = [
    "resources/config/application.yml",
]


def load_config(paths: list["str"] | None = None) -> BaseConfig:
    """
    Load configuration from a list of file paths.
    The configs are merged in order, with later files overriding earlier ones.
    If no paths are provided, defaults are used.

    :param paths: List of file paths to load configuration from.

    :return: BaseConfig instance with loaded configuration.
    """
    if paths is None:
        paths = _DEFAULT_CONFIG_PATHS
    config_data = {}
    for path in paths:
        if not os.path.exists(path):
            raise ConfigFileNotFoundException(path)
        with open(path, "r") as file:
            config_part = yaml.safe_load(file)
            if config_part:
                config_data.update(config_part)
    try:
        config_model = BaseConfig(**config_data)
        return config_model
    except ValidationError as e:
        for err in e.errors():
            print(f"Configuration validation error: {err['msg']} at {err['loc']}")
        raise ConfigException("Invalid configuration data") from e
