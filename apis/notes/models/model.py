from pydantic import BaseModel, field_validator


class NotesData(BaseModel):
    id: str
    title: str
    description: str
    completed: bool
    created_at: str
    updated_at: str
    category: str
    user_id: str


class NotesModel(BaseModel):
    success: bool
    status: int
    message: str
    data: NotesData
