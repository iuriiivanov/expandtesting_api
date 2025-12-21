from datetime import datetime
from typing import Annotated, Any, Literal

from pydantic import BaseModel, BeforeValidator, Field, field_validator

StatusInt = Annotated[
    int,
    Field(
        ...,
        pattern=r"^(200|400|401|404|500)$",
        description="Status must be one of: 200, 400, 401, 404, 500",
    ),
]

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

SuccessBool = Annotated[bool, Field(..., description="This status must be True or False only")]

DatetimeIso = Annotated[
    datetime,
    Field(..., description="Timestamp must be in ISO 8601 format"),
    BeforeValidator(lambda x: datetime.fromisoformat(x) if isinstance(x, str) else x),
]

CategoryType = Annotated[
    Literal["Home", "Work", "Personal"],
    Field(..., description="Category must be one of: Home, Work, Personal"),
]


class NoteDataModel(BaseModel):
    id: IdHex
    title: TitleStr
    description: DescriptionStr
    completed: SuccessBool
    created_at: DatetimeIso
    updated_at: DatetimeIso
    category: CategoryType
    user_id: IdHex


class NoteModel(BaseModel):
    success: SuccessBool
    status: StatusInt
    message: MessageStr
    data: NoteDataModel


class Note404Model(BaseModel):
    success: bool
    status: int
    message: str

    @field_validator("success")
    def success_status(cls, value: bool) -> bool:
        if value or value is None:
            raise ValueError("Wrong success status!")
        else:
            return value

    @field_validator("status")
    def success_status_code(cls, value: int) -> int:
        if value != 404 or value is None:
            raise ValueError("Wrong success status code!")
        else:
            return value

    @field_validator("message")
    def success_message(cls, value: str) -> str:
        if value != "No note was found with the provided ID, Maybe it was deleted" or value is None:
            raise ValueError("Wrong success message!")
        else:
            return value


class NotesModel(BaseModel):
    success: bool
    status: int
    message: str
    data: list[NoteDataModel] | None

    @field_validator("success", "status", "message")
    def fields_are_not_empty(cls, value: Any) -> Any:
        if value == "" or value is None:
            raise ValueError("The field is empty!")
        else:
            return value


class DeleteNote200Model(BaseModel):
    success: bool
    status: int
    message: str

    @field_validator("success")
    def success_status(cls, value: bool) -> bool:
        if not value or value is None:
            raise ValueError("Wrong success status!")
        else:
            return value

    @field_validator("status")
    def success_status_code(cls, value: int) -> int:
        if value != 200 or value is None:
            raise ValueError("Wrong success status code!")
        else:
            return value

    @field_validator("message")
    def success_message(cls, value: str) -> str:
        if value != "Note successfully deleted" or value is None:
            raise ValueError("Wrong success message!")
        else:
            return value


class DeleteNote400Model(BaseModel):
    success: bool
    status: int
    message: str

    @field_validator("success")
    def success_status(cls, value: bool) -> bool:
        if value or value is None:
            raise ValueError("Wrong success status!")
        else:
            return value

    @field_validator("status")
    def success_status_code(cls, value: int) -> int:
        if value != 400 or value is None:
            raise ValueError("Wrong success status code!")
        else:
            return value

    @field_validator("message")
    def success_message(cls, value: str) -> str:
        if value != "Bad Request" or value is None:
            raise ValueError("Wrong success message!")
        else:
            return value
