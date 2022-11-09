from telnetlib import SE
from app.schemas.auth import *
from sqlalchemy.orm import Session
from fastapi_jwt_auth import AuthJWT
from fastapi import HTTPException
from app.api.utils import auth as auth_utils
from app.schemas.tax import TaxCreateReq, TaxInCreate, TaxDueUpdate, TaxDue
from uuid import uuid4
from app.db import auth_crud
from app.db import tax_crud
from app.api.utils import tax as tax_utils


async def calculate_income_tax(total_income: int):

    if 0 <= total_income < 250000:
        income_tax = 0
    if 250000 < total_income <= 500000:
        income_tax = total_income * (5 / 100)
    if 500000 < total_income <= 750000:
        income_tax = 12500 + total_income * (10 / 100)
    if 750000 < total_income <= 1000000:
        income_tax = 37500 + total_income * (15 / 100)
    if 1000000 < total_income <= 1250000:
        income_tax = 75000 + total_income * (20 / 100)
    if 1250000 < total_income <= 1500000:
        income_tax = 125000 + total_income * (25 / 100)
    if total_income > 1500000:
        income_tax = 187500 + total_income * (30 / 100)

    return income_tax


async def calculate_gst(gst_percentage: int, income_manufacturing_or_service: int):
    if income_manufacturing_or_service > 0:
        gst = (income_manufacturing_or_service) * (gst_percentage / 100)
        sgst = cgst = gst / 2
    else:
        sgst = 0

    return sgst


async def create_tax(db: Session, Authorize: AuthJWT, tax_create_obj: TaxCreateReq):

    user = await auth_crud.get_user_by_email(db, tax_create_obj.email)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")
    sgst = cgst = await calculate_gst(
        tax_create_obj.gst_percentage, tax_create_obj.income_manufacturing_or_service
    )

    total_income = (
        tax_create_obj.income_manufacturing_or_service
        + tax_create_obj.income_salary
        + tax_create_obj.income_share_market
    )
    income_tax = await calculate_income_tax(total_income)
    total_tax = income_tax + tax_create_obj.fine + tax_create_obj.arrears

    tax_in_create = await make_tax_in_create_object(
        Authorize, tax_create_obj, user, sgst, cgst, total_income, income_tax, total_tax
    )
    await tax_utils.create_tax(db, tax_in_create)
    await tax_utils.create_due(db, tax_in_create, tax_create_obj)


async def make_tax_in_create_object(
    Authorize: AuthJWT,
    tax_create_obj: TaxCreateReq,
    user,
    sgst,
    cgst,
    total_income,
    income_tax,
    total_tax,
):

    tax_in_create = TaxInCreate
    tax_in_create.tax_id = str(uuid4()).replace("-", "")
    tax_in_create.uuid = user.uuid
    tax_in_create.sgst = sgst
    tax_in_create.cgst = cgst
    tax_in_create.income_manufacturing_or_service = (
        tax_create_obj.income_manufacturing_or_service
    )
    tax_in_create.income_salary = tax_create_obj.income_salary
    tax_in_create.income_share_market = tax_create_obj.income_share_market
    tax_in_create.total_income = total_income
    tax_in_create.income_tax = income_tax
    tax_in_create.arrears = tax_create_obj.arrears
    tax_in_create.fines = tax_create_obj.fine
    tax_in_create.total_tax = total_tax
    if tax_create_obj.financial_year != "string":
        tax_in_create.financial_year = tax_create_obj.financial_year
    else:
        year = tax_create_obj.due_date.strftime("%Y")
        next_year = int(year) + 1
        tax_in_create.financial_year = str(year) + "-" + str(next_year)
    tax_in_create.createdBy = Authorize.get_jwt_subject()

    return tax_in_create


async def update_due(db:Session,tax_due_update:TaxDueUpdate):

    user = await auth_crud.get_user_by_email(db,tax_due_update.email)
    if user is None:
        raise HTTPException(status_code=400, detail="User not found")

    tax= await tax_crud.get_tax(db,tax_due_update.tax_id)
    if tax is None:
        raise HTTPException(status_code=400, detail="Invalid Tax id")
    if user.uuid != tax.uuid:
        raise HTTPException(status_code=400, detail="Email and Tax id mismatch")
    taxdue = await tax_crud.get_tax_due(db,tax_due_update.tax_id)
    status=taxdue.status
    if status=="paid":
        raise HTTPException(status_code=400, detail="Invalid Operation. Cannot update due for paid tax!")
    
    await tax_utils.update_due(db,tax_due_update)

async def get_pending_tax(db:Session, Authorize:AuthJWT):

    uuid=Authorize.get_jwt_subject()
    user=await auth_crud.get_user(db,uuid)
    if user.role== 'admin' or user.role=='taxacc':
        taxdues= await tax_crud.get_pending_dues(db)

        all_tax=[]
        l=len(taxdues)
        for i in range(0,l):
            d={}
            tax_due=TaxDue
            # tax_due.due_date=taxdues[i].duedate
            # tax_due.status=taxdues[i].status
            # tax_due.tax_id=taxdues[i].tax_id
            # tax=await tax_crud.get_tax(db,tax_due.tax_id)
            # tax_due.total_tax=tax.total_tax
            # tax_due.uuid=taxdues[i].uuid
            d['tax_id']=taxdues[i].tax_id
            d['uuid']=taxdues[i].uuid
            d['due_date']=taxdues[i].duedate
            d['status']=taxdues[i].status
            tax=await tax_crud.get_tax(db,taxdues[i].tax_id)
            d['total_tax']=tax.total_tax

            print(d)
            all_tax.append(d)

        return all_tax
    taxdues= await tax_crud.get_pending_dues(db,uuid=uuid)
    
    
    all_tax=[]
    l=len(taxdues)
    for i in range(0,l):
        d={}
        tax_due=TaxDue
        # tax_due.due_date=taxdues[i].duedate
        # tax_due.status=taxdues[i].status
        # tax_due.tax_id=taxdues[i].tax_id
        # tax=await tax_crud.get_tax(db,tax_due.tax_id)
        # tax_due.total_tax=tax.total_tax
        # tax_due.uuid=taxdues[i].uuid
        d['tax_id']=taxdues[i].tax_id
        d['uuid']=taxdues[i].uuid
        d['due_date']=taxdues[i].duedate
        d['status']=taxdues[i].status
        tax=await tax_crud.get_tax(db,taxdues[i].tax_id)
        d['total_tax']=tax.total_tax

        print(d)
        all_tax.append(d)

    return all_tax

async def get_tax(db:Session,Authorize:AuthJWT,tax_id:str):

    uuid=Authorize.get_jwt_subject()
    tax=await tax_crud.get_tax(db,tax_id)
    if tax.uuid != uuid:
        return None
    taxdue=await tax_crud.get_tax_due(db,tax_id)
    # x= TaxInCreate
    x={}
    x['due_date']=taxdue.duedate
    x['status']=taxdue.status
    x['tax_id']=tax_id
    x['uuid']=uuid
    x['total_tax']=tax.total_tax
    x['sgst']=tax.sgst
    x['cgst']=tax.cgst
    x['income_manufacturing_or_service']=tax.income_manufacturing_or_service
    x['income_salary']=tax.income_salary
    x['income_share_market']=tax.income_share_market
    x['total_income']=tax.total_income
    x['arrears']=tax.arrears
    x['fines']=tax.fines
    x['financial_year']=tax.financial_year
    x['createdBy']=tax.createdBy

    return x

async def pay_tax(db:Session, Authorize:AuthJWT,tax_id:str):

    uuid=Authorize.get_jwt_subject()
    tax=await tax_crud.get_tax(db,tax_id)
    if tax.uuid != uuid:
        raise HTTPException(status_code=400, detail="Invaid Tax id")

    await tax_utils.pay_tax(db,tax_id)

async def get_taxes(db:Session, Authorize:AuthJWT):

    uuid=Authorize.get_jwt_subject()
    user=await auth_crud.get_user(db,uuid)
    
    