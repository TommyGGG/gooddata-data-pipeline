from pathlib import Path
from typing import Any, Dict, Type, TypeVar
import attrs
from cattrs import structure
from enum import Enum


class GoodDataLdmTypes(Enum):
    PRIMARY_KEY = "primary_key"
    REFERENCE = "reference"
    DATE = "date"
    FACT = "fact"
    ATTRIBUTE = "attribute"
    LABEL = "label"


DATE_GRANULARITIES = [
    "DAY",
    "WEEK",
    "MONTH",
    "QUARTER",
    "YEAR",
    "DAY_OF_WEEK",
    "DAY_OF_MONTH",
    "DAY_OF_YEAR",
    "WEEK_OF_YEAR",
    "MONTH_OF_YEAR",
    "QUARTER_OF_YEAR",
]
TIMESTAMP_GRANULARITIES = [
    "MINUTE",
    "HOUR",
    "MINUTE_OF_HOUR",
    "HOUR_OF_DAY",
]
T = TypeVar("T", bound="Base")

DBT_PATH_TO_MANIFEST = Path("target") / "manifest.json"

class DbtTests(Enum):
    PRIMARY_KEY = "dbt_constraints.primary_key"
    FOREIGN_KEY = "dbt_constraints.foreign_key"
    FOREIGN_KEY_REF = "pk_table_name"

DATETIME_DATA_TYPES = [
    "DATE",
    "TIMESTAMP",
    "TIMESTAMPTZ"
]

TIMESTAMP_DATA_TYPES = [
    "TIMESTAMP",
    "TIMESTAMPTZ"
]

@attrs.define
class Base:
    @classmethod
    def from_dict(cls: Type[T], data: Dict[str, Any]) -> T:
        """
        Creates object from dictionary.
        """
        return structure(data, cls)

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts object into dictionary.
        """
        return attrs.asdict(self)
