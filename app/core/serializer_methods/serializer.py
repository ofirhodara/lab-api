from typing import Dict, Any
from result import Ok, Err
from abc import ABC, abstractmethod
from enum import Enum

from app.core.lab.laboratory import LabDataItem
from app.managers.logger_manager import create_logger

logger = create_logger(__name__)


class DataFormat(str, Enum):
    """
        Enumeration of data formats.
        I inherited str also because a trouble with pydantic and enum evaluation.
    """
    JSON = "json"
    XML = "xml"
    CSV = "csv"
    YAML = "yml"


class IBaseSerializer(ABC):
    """Abstract base class for serializers."""

    @abstractmethod
    def parse(self, data: Any, target_class: LabDataItem) -> any:
        """Parse data into target_class.

        Args:
            data: The data to be parsed.
            target_class: The target class to parse the data into.

        Returns:
            Parsed data as an instance of target_class.
        """
        pass
