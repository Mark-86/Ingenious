from re import L
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, root_validator
import datetime


class TaxCreateReq(BaseModel):

    email: str
    pan_number: str
    income_salary: Optional[int]
    income_manufacturing_or_service: Optional[int]
    gst_percentage: Optional[int] = 18
    income_share_market: Optional[int]
    arrears: Optional[int]
    fine: Optional[int]
    financial_year: str
    due_date: datetime.date


class TaxInCreate(BaseModel):
    tax_id: str
    uuid: str
    sgst: int
    cgst: int
    income_manufacturing_or_service: int
    income_salary: int
    income_share_market: int
    total_income: int
    income_tax: int
    arrears: int
    fines: int
    total_tax: int
    financial_year: str
    createdBy: str


class TaxDueUpdate(BaseModel):
    email:str
    tax_id: str
    new_due: datetime.date

class TaxDue(BaseModel):
    
    tax_id: str
    uuid: str
    total_tax: int
    due_date: datetime.date
    status: str