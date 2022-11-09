from fastapi import APIRouter, Depends, Header, Response, status, HTTPException
from fastapi_jwt_auth import AuthJWT
from app.schemas.auth import *
from sqlalchemy.orm import Session
from app.db import get_db
from app.db import auth_crud
from app.api.controllers import auth as auth_controller
from app.api.controllers import user as user_controller
from app.api.controllers import tax as tax_controller
from app.api.lib.auth import check_role_permission
from app.schemas.tax import TaxCreateReq, TaxDueUpdate

router = APIRouter()


# @router.post("/create_tax")
# async def create_tax(
#     tax_create_obj: TaxCreateReq,
#     Authorize: AuthJWT = Depends(),
#     Authorization: Optional[str] = Header(None),
#     db: Session = Depends(get_db),
# ):
#     Authorize.jwt_required()
#     await check_role_permission(db, Authorize, ["taxacc"])

#     await tax_controller.create_tax(db, Authorize, tax_create_obj)


# @router.post("/update_due")
# async def update_due(
#     tax_due_update: TaxDueUpdate,
#     Authorize: AuthJWT = Depends(),
#     Authorization: Optional[str] = Header(None),
#     db: Session = Depends(get_db),
# ):
#     Authorize.jwt_required()
#     await check_role_permission(db, Authorize, ["taxacc"])

#     await tax_controller.update_due(db,tax_due_update)

# @router.get("/get_pending_tax")
# async def get_pending_tax(
#     Authorize: AuthJWT = Depends(),
#     Authorization: Optional[str] = Header(None),
#     db: Session = Depends(get_db),
# ):
#     Authorize.jwt_required()

#     return await tax_controller.get_pending_tax(db,Authorize)


# @router.get("/get_tax")
# async def get_tax(
#     tax_id: str,
#     Authorize: AuthJWT = Depends(),
#     Authorization: Optional[str] = Header(None),
#     db: Session = Depends(get_db),
# ):

#     Authorize.jwt_required()
#     return await tax_controller.get_tax(db,Authorize,tax_id)

# @router.post("/pay_tax")
# async def pay_tax(
#     tax_id: str,
#     Authorize: AuthJWT = Depends(),
#     Authorization: Optional[str] = Header(None),
#     db: Session = Depends(get_db),
# ):

#     Authorize.jwt_required()
#     await tax_controller.pay_tax(db,Authorize,tax_id)

# @router.post("/get_taxes")
# async def get_tax(
#     Authorize: AuthJWT = Depends(),
#     Authorization: Optional[str] = Header(None),
#     db: Session = Depends(get_db),
# ):

#     Authorize.jwt_required()
#     return await tax_controller.get_taxes(db,Authorize,)