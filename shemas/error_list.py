from typing import Optional

from pydantic import BaseModel, ConfigDict


class Ctx(BaseModel):

    model_config = ConfigDict(extra='forbid')

    ge: Optional[int] = None
    le: Optional[int] = None


class ErrorParam(BaseModel):

    model_config = ConfigDict(extra='forbid')

    type: str
    loc: list[str]
    msg: str
    input: str
    ctx: Optional[Ctx] = None


class ErrorParams(BaseModel):

    model_config = ConfigDict(extra='forbid')

    detail: list[ErrorParam]
