from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="taxpayer")
    # is_active = Column(Boolean, default=True)


class UserTokens(Base):

    __tablename__ = "usertokens"

    uuid = Column(String, primary_key=True)
    access_token = Column(String)
    refresh_token = Column(String)
