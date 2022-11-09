from tkinter.messagebox import NO
from fastapi import APIRouter, Depends, Header, Response, status, HTTPException
from fastapi_jwt_auth import AuthJWT
from app.schemas.auth import *
from sqlalchemy.orm import Session
from app.db import get_db
from app.db import auth_crud
from app.api.controllers import auth as auth_controller
from app.api.controllers import user as user_controller
from app.api.lib.auth import check_role_permission
from app.schemas.user import UpdateRole, TaxPayersReq


router = APIRouter()


@router.get("/get_user")
async def get_user(
    Authorize: AuthJWT = Depends(),
    Authorization: Optional[str] = Header(None),
):
    Authorize.jwt_required()
    return Authorize.get_jwt_subject()


@router.get("/get_users")
async def get_user(
    Authorize: AuthJWT = Depends(),
    Authorization: Optional[str] = Header(None),
    db: Session = Depends(get_db),
):
    Authorize.jwt_required()
    await check_role_permission(db, Authorize, ["admin"])
    return await user_controller.get_users(db)


# @router.post("/update_role")
# async def update_role(
#     update_role_obj: UpdateRole,
#     Authorize: AuthJWT = Depends(),
#     Authorization: Optional[str] = Header(None),
#     db: Session = Depends(get_db),
# ):
#     Authorize.jwt_required()
#     await check_role_permission(db, Authorize, ["admin"])

#     # uuid = Authorize.get_jwt_subject()
#     return await user_controller.update_role(
#         db, update_role_obj.email, update_role_obj.old_role, update_role_obj.new_role
#     )


# @router.get("/get_tax_payers")
# async def get_tax_payers(
#     tax_payer_obj: TaxPayersReq,
#     Authorize: AuthJWT = Depends(),
#     Authorization: Optional[str] = Header(None),
#     db: Session = Depends(get_db),
# ):
#     print(tax_payer_obj)
#     Authorize.jwt_required()
#     await check_role_permission(db, Authorize, ["taxacc"])

#     return await user_controller.get_tax_payers(
#         db, tax_payer_obj.page, tax_payer_obj.per_page
#     )
