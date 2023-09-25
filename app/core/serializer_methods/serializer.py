from typing import Dict
from result import Ok, Err
from abc import ABC, abstractmethod
from enum import Enum

from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


class DataFormat(str, Enum):
    """Enumeration of data formats."""
    JSON = "json"
    XML = "xml"
    CSV = "csv"
    YAML = "yaml"


class IBaseSerializer(ABC):
    """Abstract base class for serializers."""

    @abstractmethod
    def parse(self, data, target_class) -> any:
        """Parse data into target_class.

        Args:
            data: The data to be parsed.
            target_class: The target class to parse the data into.

        Returns:
            Parsed data as an instance of target_class.
        """
        pass

