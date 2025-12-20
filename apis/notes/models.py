from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, field_validator


class NoteDataModel(BaseModel):
    id: str = Field(
        ...,
        description="The Node ID must be 24 characters long and consist only of characters from the set: '0123456789abcdef'",
        pattern=r"^[a-f0-9]{24}$",
    )
    title: str = Field(
        ..., min_length=4, max_length=100, description="Title must be between 4 and 100 characters"
    )
    description: str = Field(
        ...,
        min_length=4,
        max_length=1000,
        description="Description must be between 4 and 1000 characters",
    )
    completed: bool = Field(..., description="The completed status must be True or False only")
    created_at: datetime = Field(..., description="Timestamp muct be in ISO 8601 format")
    updated_at: datetime = Field(..., description="Timestamp must be in ISO 8601 format")
    category: str = Field(
        ...,
        pattern=r"^(Home|Work|Personal)$",
        description="Category must be one of: Home, Work, Personal",
    )
    user_id: str = Field(..., description="Note ID", pattern=r"^[a-f0-9]{24}$")


class NoteModel(BaseModel):
    success: bool = True | False
    status: int
    message: str
    data: NoteDataModel

    @field_validator("success", "status", "message")
    def fields_are_not_empty(cls, value: Any) -> Any:
        if value == "" or value is None:
            raise ValueError("The field is empty!")
        else:
            return value


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
