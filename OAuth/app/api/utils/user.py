from uuid import uuid4
from app.db import auth_crud
from app.schemas.auth import UserInCreate, UserInDB, UserBase, UserTokens
from sqlalchemy.orm import Session
from app.api.lib.auth import AuthHandler
from fastapi_jwt_auth import AuthJWT
from app.models import auth as auth_models


async def update_role(db: Session, email: str, new_role: str):

    user = db.query(auth_models.User).filter(auth_models.User.email == email).first()
    user.role = new_role
    db.add(user)
    db.commit()
    db.refresh(user)

    return user
