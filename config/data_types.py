from datetime import datetime
from typing import Annotated, Literal

from pydantic import BeforeValidator, Field

SuccessBool = Annotated[bool, Field(..., description="This status must be True or False only")]

StatusInt = Annotated[int, Field(..., description="Status must be one of: 200, 400, 401, 404, 500")]

MessageStr = Annotated[str, Field(..., description="Note status message")]

IdHex = Annotated[
    str,
    Field(
        ...,
        description="The ID must be 24 characters long and consist only of hexadecimal characters",
        pattern=r"^[a-f0-9]{24}$",
    ),
]

TitleStr = Annotated[
    str,
    Field(
        ..., min_length=4, max_length=100, description="Title must be between 4 and 100 characters"
    ),
]

DescriptionStr = Annotated[
    str,
    Field(
        ...,
        min_length=4,
        max_length=1000,
        description="Description must be between 4 and 1000 characters",
    ),
]

DateTimeIso = Annotated[
    datetime,
    Field(..., description="Timestamp must be in ISO 8601 format"),
    BeforeValidator(lambda x: datetime.fromisoformat(x) if isinstance(x, str) else x),
]

CategoryType = Annotated[
    Literal["Home", "Work", "Personal"],
    Field(..., description="Category must be one of: Home, Work, Personal"),
]
