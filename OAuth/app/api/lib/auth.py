from passlib.context import CryptContext
from functools import wraps
import json
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi import Depends, HTTPException
from app.models import auth as models
from sqlalchemy.orm import Session

# import
class AuthHandler:

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)


def auth_check(roles):
    def decorator_auth(func):
        @wraps(func)
        def wrapper_auth(*args, **kwargs):
            Authorize = kwargs["Authorize"]
            db = kwargs["db"]
            Authorize.jwt_required()
            current_user = Authorize.get_jwt_subject()
            print(current_user)
            role = json.loads(current_user)
            print(role["role"])
            # user_role = db.query(models.UserRole).filter(
            #     models.UserRole.user_id == role["id"]).first()
            # print(user_role.role_name)
            # role_names = user_role.role_name
            # role_in_db = role_names.split(",")

            if role["role"] in roles:
                return func(*args, **kwargs)
            return JSONResponse(status_code=401, content={"detail": "Unauthorized"})

        return wrapper_auth

    return decorator_auth


async def check_role_permission(
    db: Session, Authorize: AuthJWT, required_roles: list[str]
):

    current_user = Authorize.get_jwt_subject()
    user_role = db.query(models.User).filter(models.User.uuid == current_user).first()
    role = user_role.role
    if role == "admin":
        return True
    if role not in required_roles:

        raise HTTPException(status_code=403, detail="Unauthorized")
