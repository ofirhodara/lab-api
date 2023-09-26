import functools
from abc import ABC, abstractmethod
from typing import Any

from app.core.lab.laboratory import LabDataItem
from app.exceptions.lab_exceptions import SerializationError
from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


def handle_serialize_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except SerializationError as e:
            logger.fatal(e)
            raise e
        except Exception as e:
            logger.fatal(e)
            raise e

    return wrapper


class IBaseSerializer(ABC):
    """Abstract base class for serializers."""

    @handle_serialize_error
    @abstractmethod
    def serialize(self, data: Any, target_class: LabDataItem) -> any:
        """Parse data into target_class.

        Args:
            data: The data to be parsed.
            target_class: The target class to parse the data into.

        Returns:
            Parsed data as an instance of target_class.
        """
        pass
