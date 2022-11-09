from app.schemas.auth import *
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from fastapi import HTTPException
from app.api.utils import auth as auth_utils
from app.api.lib.auth import AuthHandler


from app.db import auth_crud


async def register_new_user(
    user_create_obj: UserCreateReq, db: Session, Authorize: AuthJWT
):

    db_user = await auth_crud.get_user_by_email(db, email=user_create_obj.email)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exist")

    user = await auth_utils.register_new_user(user_create_obj, db)

    if user:
        tokens = await gen_and_save_tokens(user.uuid, Authorize, db)

    user = user.dict()
    user["tokens"] = {
        "access_token": tokens["access_token"],
        "refresh_token": tokens["refresh_token"],
    }

    user_res = RegisterRes(**user)
    return user_res


async def login(login_req_obj: UserLoginReq, db: Session, Authorize: AuthJWT):

    db_user = await auth_crud.get_user_by_email(db, email=login_req_obj.email)
    if db_user:
        auth = AuthHandler()
        verified = auth.verify_password(login_req_obj.password, db_user.hashed_password)
        if verified:
            tokens = await gen_and_save_tokens(db_user.uuid, Authorize, db)
            tokens["uuid"] = db_user.uuid
            return tokens
        else:
            raise HTTPException(status_code=403, detail="Invalid Credentials")
    else:
        raise HTTPException(status_code=404, detail="User not found")


async def gen_and_save_tokens(uuid: str, Authorize: AuthJWT, db: Session) -> dict:
    tokens = await auth_utils.create_access_and_refresh_token(
        Authorize=Authorize, uuid=uuid, db=db
    )

    await auth_utils.save_tokens(db, uuid, tokens)
    return tokens


async def gen_access_token_from_refresh_token(
    uuid: str,
    Authorize: AuthJWT,
    db: Session,
    Authorization: str,
) -> dict:
    new_access_token = await auth_utils.create_access_token(Authorize, uuid=uuid, db=db)
    tokens = {
        "access_token": new_access_token,
        "refresh_token": Authorization.split("Bearer ")[1].strip(),
    }
    await auth_utils.save_tokens(db, uuid, tokens)
    return tokens
