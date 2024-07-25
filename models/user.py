from typing import List, Optional

from pydantic import BaseModel, EmailStr, HttpUrl, Extra, RootModel


class User(BaseModel, extra=Extra.forbid):
    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl


class Users(BaseModel, extra=Extra.forbid):
    items: list[Optional[User]]
    total: int
    page: int
    size: int
    pages: int


