from typing import List, Optional

from pydantic import BaseModel, EmailStr, HttpUrl, Extra, RootModel


class Ctx(BaseModel, extra=Extra.forbid):
    ge: Optional[int] = None
    le: Optional[int] = None


class ErrorParam(BaseModel, extra=Extra.forbid):
    type: str
    loc: list[str]
    msg: str
    input: str
    ctx: Optional[Ctx] = None


class ErrorParams(BaseModel, extra=Extra.forbid):
    detail: list[ErrorParam]
