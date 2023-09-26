from enum import Enum


class DataFormat(str, Enum):
    """
        Enumeration of data formats.
        I inherited str also because a trouble with pydantic and enum evaluation.
    """
    JSON = "json"
    XML = "xml"
    CSV = "csv"
    YAML = "yml"
