import secrets

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    username: str = Field(unique=True, index=True)
    is_active: bool = Field(default=True)


class UserCreate(UserBase):
    pass


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    api_key: str = Field(default_factory=lambda: secrets.token_urlsafe(32), index=True)
    tokens: int = Field(default=30)


class UserPublic(UserBase):
    id: int
    api_key: str
