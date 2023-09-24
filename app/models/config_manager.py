import sys
from pathlib import Path

import piny.errors as pe
from piny import YamlLoader

DEFAULT_CONFIG_PATH = Path("core/config/config.yaml")


class ConfigurationManager:
    _instance = None

    def __new__(cls, config_file: Path = DEFAULT_CONFIG_PATH):
        """
        Create a new instance of ConfigurationManager.

        Args:
            config_file (Path): Path to the configuration file (default is DEFAULT_CONFIG_PATH).

        Returns:
            ConfigurationManager: A configured instance of ConfigurationManager.
        """
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance._config = cls._load_config(config_file)
        return cls._instance

    @staticmethod
    def _load_config(config_path: Path):
        """
        Load configuration from a YAML file.

        Args:
            config_path (Path): Path to the configuration file.

        Returns:
            dict: A dictionary containing the loaded configuration.

        Raises:
            pe.LoadingError: If there is an issue loading the configuration.
            pe.ConfigError: If there is an issue with the configuration format.
        """
        try:
            return YamlLoader(path=config_path.__str__()).load()
        except (pe.LoadingError, pe.ConfigError) as e:
            # Consider logging the error or raising a custom exception here
            sys.exit(e)

    def get_config(self):
        """
        Get the loaded configuration.

        Returns:
            dict: A dictionary containing the loaded configuration.
        """
        return self._instance._config
