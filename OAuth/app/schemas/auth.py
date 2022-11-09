from typing import Any, Dict, List, Optional
from pydantic import BaseModel, root_validator
import datetime


class UserBase(BaseModel):
    email: str


class UserCreateReq(UserBase):
    password: str


class UserLoginReq(UserBase):
    password: str


class UserInCreate(UserBase):
    uuid: str
    hashed_password: str
    role: str = "taxpayer"

    class Config:
        orm_mode = True


class UserInDB(UserInCreate):
    id: int

    class Config:
        orm_mode = True


class UserRes(UserBase):
    uuid: str
    role: str


class RegisterRes(UserRes):
    tokens: dict


class Tokens(BaseModel):
    access_token: str
    refresh_token: str


class UserTokens(Tokens):
    uuid: str
