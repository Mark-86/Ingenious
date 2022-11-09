from app.schemas.auth import *
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from fastapi import HTTPException
from app.api.utils import auth as auth_utils
from app.api.lib.auth import AuthHandler
from app.db import auth_crud
from app.api.utils import user as user_utils
from app.schemas.auth import UserRes


async def update_role(db: Session, email: str, old_role: str, new_role: str):

    user = await auth_crud.get_user_by_email(db, email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    if user.role != old_role:
        raise HTTPException(status_code=400, detail="Old role does not match")

    user = await user_utils.update_role(db, email, new_role)
    data = {}
    data["uuid"] = user.uuid
    data["email"] = user.email
    data["role"] = user.role

    return UserRes(**data)


async def get_users(db: Session):
    users = await auth_crud.get_users(db, skip=2, limit=10)
    print(len(users))
    return users


async def get_tax_payers(db: Session, page: int, per_page: int):
    skip = 10 * page - 10
    tax_payers = await auth_crud.get_tax_payers(db, skip, per_page)

    return tax_payers
