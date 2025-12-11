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
