from pydantic import BaseModel, ConfigDict, EmailStr, HttpUrl, conlist


class User(BaseModel):

    model_config = ConfigDict(extra='forbid')

    id: int
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl


class Users(BaseModel):
    """Из-за особенности пагинации, что используем в ендпоинте тут модель выглядит не как оригинал.

    Посмотрел по коду, как менять модель в пагинации и там на первый взгляд это не так просто
    окозалось, поэтому решил пока так оставить. Чтобы было ясно, там нужно в класс пагинации что-то
    переназначить/указывать, чтобы он иначе обрабатывал пагинацию
    """

    model_config = ConfigDict(extra='forbid')

    items: list[User] | conlist(None, max_length=0)
    total: int
    page: int
    size: int
    pages: int
