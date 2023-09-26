"""
Module: configuration_manager.py

This module defines a `ConfigurationManager` class for managing application configuration settings.

"""

import sys
from pathlib import Path

import piny.errors as pe
from piny import YamlLoader

DEFAULT_CONFIG_PATH = Path("app/config/config.yml")


class ConfigurationManager:
    """
    The `ConfigurationManager` class manages application configuration settings.

    Attributes:
        _instance (ConfigurationManager): The single instance of ConfigurationManager.
        _config (dict): The configuration settings loaded from a YAML file.

    Methods:
        __new__: Create a new instance of ConfigurationManager (Singleton pattern).
        get_instance: Get the existing instance of ConfigurationManager.
        _load_config: Load configuration settings from a YAML file.
        get_config: Get the loaded configuration settings.

    """

    _instance = None

    def __new__(cls, config_file: Path):
        """
        Create a new instance of ConfigurationManager.

        Args:
            config_file (Path): Path to the configuration file (default is DEFAULT_CONFIG_PATH).

        Returns:
            ConfigurationManager: A configured instance of ConfigurationManager.
        """
        if cls._instance is None:
            if config_file is None:
                config_file = DEFAULT_CONFIG_PATH
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance._config = cls._load_config(config_file)
        return cls._instance

    @classmethod
    def get_instance(cls):
        """
        Get the existing instance of ConfigurationManager.

        Returns:
            ConfigurationManager: The existing instance of ConfigurationManager.
        """
        if cls._instance is None:
            raise ValueError("ConfigurationManager instance has not been created yet.")
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
            print(config_path)
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
