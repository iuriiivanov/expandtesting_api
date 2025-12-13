from typing import Any

from pydantic import BaseModel, field_validator


class NoteData(BaseModel):
    id: str
    title: str
    description: str
    completed: bool
    created_at: str
    updated_at: str
    category: str
    user_id: str

    @field_validator(
        "id", "title", "description", "completed", "created_at", "updated_at", "category", "user_id"
    )
    def fields_are_not_empty(cls, value: Any) -> Any:
        if value == "" or value is None:
            raise ValueError("The field is empty!")
        else:
            return value


class NoteModel(BaseModel):
    success: bool
    status: int
    message: str
    data: NoteData

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
    data: list[NoteData] | None

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
