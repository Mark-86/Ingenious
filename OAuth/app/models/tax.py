import uuid
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.database import Base
import datetime


class Tax(Base):

    __tablename__ = "tax"

    id = Column(Integer, primary_key=True)
    tax_id = Column(String, unique=True)
    uuid = Column(String)
    sgst = Column(Integer, default=0)
    cgst = Column(Integer, default=0)
    income_manufacturing_or_service = Column(Integer, default=0)
    income_salary = Column(Integer, default=0)
    income_share_market = Column(Integer, default=0)
    total_income = Column(Integer, default=0)
    income_tax = Column(Integer, default=0)
    arrears = Column(Integer, default=0)
    fines = Column(Integer, default=0)
    total_tax = Column(Integer, default=0)
    financial_year = Column(String)
    createdAt = Column(DateTime, default=datetime.datetime.now())
    createdBy = Column(String)


class TaxDue(Base):

    __tablename__ = "taxdue"

    id = Column(Integer, primary_key=True)
    tax_id = Column(String, unique=True)
    uuid = Column(String)
    duedate = Column(DateTime, default=datetime.date)
    status = Column(String, default="new")  # New / Paid / Delay
    createdAt = Column(DateTime, default=datetime.datetime.now())
    duedate_update = Column(DateTime, default=datetime.datetime.now())
