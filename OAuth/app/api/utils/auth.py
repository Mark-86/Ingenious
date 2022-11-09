from uuid import uuid4
from app.db import auth_crud
from app.schemas.auth import UserInCreate, UserInDB, UserBase, UserTokens
from sqlalchemy.orm import Session
from app.api.lib.auth import AuthHandler
from fastapi_jwt_auth import AuthJWT


async def register_new_user(user_crete_obj: UserBase, db: Session):

    auth = AuthHandler()
    uuid = str(uuid4()).replace("-", "")
    hashed_password = auth.get_password_hash(user_crete_obj.password)
    data = {}
    data["email"] = user_crete_obj.email
    data["hashed_password"] = hashed_password
    data["uuid"] = uuid

    user_in_create = UserInCreate(**data)

    await auth_crud.create_user(db, user_in_create)

    return user_in_create


async def get_token_user_claims(uuid: str, db: Session) -> dict:
    user_claims = {}

    user_details = await auth_crud.get_user(db, uuid)
    # user_details: UserFromDB = await user_utils.get_user_detail_from_uuid(uuid, mongodb)
    user_claims["role"] = user_details.role
    return user_claims


async def create_access_and_refresh_token(
    Authorize: AuthJWT, uuid: str, db: Session
) -> dict:

    access_token = await create_access_token(Authorize, uuid=uuid, db=db)

    # TODO: Save refresh token in database
    refresh_token = await create_refresh_token(Authorize, uuid=uuid, db=db)
    return {"access_token": access_token, "refresh_token": refresh_token}


async def create_access_token(
    Authorize: AuthJWT, uuid: str, db: Session, expires_time: int = 3600
) -> str:
    user_claims = await get_token_user_claims(uuid, db)
    return Authorize.create_access_token(
        subject=uuid, user_claims=user_claims, expires_time=expires_time
    )


async def create_refresh_token(Authorize: AuthJWT, uuid: str, db: Session) -> str:
    user_claims = await get_token_user_claims(uuid, db)
    return Authorize.create_refresh_token(subject=uuid, user_claims=user_claims)


async def save_tokens(db: Session, uuid: str, tokens: dict):

    old_token = await auth_crud.get_token(db, uuid)

    if old_token:
        await auth_crud.update_refresh_and_access_token(
            db, uuid, tokens["access_token"], tokens["refresh_token"]
        )
    else:
        data = {}
        data["uuid"] = uuid
        data["access_token"] = tokens["access_token"]
        data["refresh_token"] = tokens["refresh_token"]

        user_tokens = UserTokens(**data)

        await auth_crud.create_token(db, user_tokens)
