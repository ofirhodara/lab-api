import logging
from logging.handlers import RotatingFileHandler

from app.models.config_manager import ConfigurationManager


def create_logger(module_name: str) -> logging.Logger:
    """
    Create and configure a logger for a specific module.

    This function sets up a logger with options specified in the configuration file,
    including log level, log formatting, console output, and file rotation.

    Args:
        module_name (str): The name of the module or component for which the logger is created.

    Returns:
        logging.Logger: A configured logger instance ready for use.

    Example:
        To create a logger for a module called 'my_module', use the following code:

        >>> logger = create_logger('my_module')
        >>> logger.info('This is an informational log message.')

    """
    # Get the logging configuration from the ConfigurationManager
    config_logger = ConfigurationManager().get_config()["logging"]

    # Create a logger with the specified module name
    logger = logging.getLogger(module_name)

    # Set the log level based on the configuration
    log_level = config_logger["log_level"]
    logger.setLevel(log_level)

    # Define the log message format
    log_formatter = logging.Formatter("[%(asctime)s] - [%(name)s] - [%(levelname)s]: %(message)s")

    # Create a console handler for log output to the console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    logger.addHandler(console_handler)

    # Create a file handler with log rotation based on configuration
    file_handler = RotatingFileHandler(
        filename=config_logger["filename"],
        maxBytes=int(config_logger["max_bytes"]),
        backupCount=int(config_logger["backup_count"]),
        encoding=config_logger["encoding"]
    )

    file_handler.setFormatter(log_formatter)
    logger.addHandler(file_handler)

    return logger
