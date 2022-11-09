import uu
from fastapi import APIRouter, Depends, Header, Response, status, HTTPException
from fastapi_jwt_auth import AuthJWT
from app.schemas.auth import *
from sqlalchemy.orm import Session
from app.db import get_db
from app.db import auth_crud
from app.api.controllers import auth as auth_controller
from app.api.controllers import user as user_controller
from app.api.lib.auth import check_role_permission


router = APIRouter()


@router.post("/register")
async def register(
    user_create_obj: UserCreateReq,
    db: Session = Depends(get_db),
    Authorize: AuthJWT = Depends(),
):
    res = await auth_controller.register_new_user(user_create_obj, db, Authorize)
    return res


@router.post("/login", status_code=200)
async def login(
    user_login_obj: UserLoginReq,
    db: Session = Depends(get_db),
    Authorize: AuthJWT = Depends(),
):
    return await auth_controller.login(user_login_obj, db, Authorize)


@router.get(
    "/gen_access_token",
)
async def gen_access_token(
    Authorize: AuthJWT = Depends(),
    Authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    """
    Takes a refresh token and return a access token
    after checking if the refresh token is valid.
    """
    Authorize.jwt_refresh_token_required()
    uuid = Authorize.get_jwt_subject()
    tokens = await auth_controller.gen_access_token_from_refresh_token(
        uuid, Authorize, db, Authorization
    )
    return tokens
