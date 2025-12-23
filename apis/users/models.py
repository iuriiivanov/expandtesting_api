from typing import Any

from pydantic import BaseModel, field_validator


class UserDataModel(BaseModel):
    id: int
    name: str
    email: str

    @field_validator("id", "name", "email")
    def fields_are_not_empty(cls, value: Any) -> Any:
        if value == "" or value is None:
            raise ValueError("The field is empty!")
        else:
            return value


class UserModel(BaseModel):
    success: bool
    status: int
    message: str
    data: UserDataModel

    @field_validator("success", "status", "message")
    def fields_are_not_empty(cls, value: Any) -> Any:
        if value == "" or value is None:
            raise ValueError("The field is empty!")
        else:
            return value


class UserProfileDataModel(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    company: str

    @field_validator("id", "name", "email")
    def fields_are_not_empty(cls, value: Any) -> Any:
        if value == "" or value is None:
            raise ValueError("The field is empty!")
        else:
            return value


class UserProfileModel(BaseModel):
    success: bool
    status: int
    message: str
    data: UserProfileDataModel

    @field_validator("success", "status", "message")
    def fields_are_not_empty(cls, value: Any) -> Any:
        if value == "" or value is None:
            raise ValueError("The field is empty!")
        else:
            return value
