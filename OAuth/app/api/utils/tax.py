from uuid import uuid4
from app.db import auth_crud
from app.schemas.tax import TaxInCreate
from sqlalchemy.orm import Session
from app.api.lib.auth import AuthHandler
from app.schemas.tax import TaxCreateReq, TaxDueUpdate
from fastapi_jwt_auth import AuthJWT
from app.models import tax as tax_models
import datetime
from fastapi import HTTPException


async def create_tax(db: Session, tax_in_create: TaxInCreate):

    tax = tax_models.Tax(
        tax_id=tax_in_create.tax_id,
        uuid=tax_in_create.uuid,
        sgst=tax_in_create.sgst,
        cgst=tax_in_create.cgst,
        income_manufacturing_or_service=tax_in_create.income_manufacturing_or_service,
        income_salary=tax_in_create.income_salary,
        income_share_market=tax_in_create.income_share_market,
        total_income=tax_in_create.total_income,
        income_tax=tax_in_create.income_tax,
        arrears=tax_in_create.arrears,
        fines=tax_in_create.fines,
        total_tax=tax_in_create.total_tax,
        financial_year=tax_in_create.financial_year,
        createdAt=datetime.datetime.now(),
        createdBy=tax_in_create.createdBy,
    )

    db.add(tax)
    db.commit()
    db.refresh(tax)
    return tax


async def create_due(
    db: Session, tax_in_create: TaxInCreate, tax_create_obj: TaxCreateReq
):
    status = "new"
    # if tax_create_obj.due_date<datetime.datetime.now():
    #     status = "delay"
    taxdue = tax_models.TaxDue(
        tax_id=tax_in_create.tax_id,
        uuid=tax_in_create.uuid,
        duedate=tax_create_obj.due_date,
        status=status,
        duedate_update=datetime.datetime.now(),
    )

    db.add(taxdue)
    db.commit()
    db.refresh(taxdue)
    return taxdue

async def update_due(db: Session, tax_due_update:TaxDueUpdate):

    taxdue= db.query(tax_models.TaxDue).filter(tax_models.TaxDue.tax_id == tax_due_update.tax_id).first()

    taxdue.duedate = tax_due_update.new_due
    taxdue.duedate_update=datetime.datetime.now()

    db.add(taxdue)
    db.commit()
    db.refresh(taxdue)
    return taxdue

async def pay_tax(db: Session, tax_id:str):

    due=  taxdue= db.query(tax_models.TaxDue).filter(tax_models.TaxDue.tax_id == tax_id).first()

    if due.status == 'paid':
        raise HTTPException(status_code=400, detail="Tax already paid")
    due.status='paid'

    db.add(due)
    db.commit()
    db.refresh(due)
    return due