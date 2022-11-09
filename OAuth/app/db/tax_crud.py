from sqlalchemy.orm import Session
from app.models import tax  as tax_models

async def get_tax(db: Session, tax_id: str):
    return db.query(tax_models.Tax).filter(tax_models.Tax.tax_id == tax_id).first()

async def get_taxes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(tax_models.Tax).offset(skip).limit(limit).all()

async def get_tax_due(db: Session, tax_id: str):
    return db.query(tax_models.TaxDue).filter(tax_models.TaxDue.tax_id == tax_id).first()

async def get_tax_dues(db: Session, skip: int = 0, limit: int = 100,uuid: str=None):
    if uuid:
        return db.query(tax_models.TaxDue).filter(tax_models.TaxDue.uuid == uuid).offset(skip).limit(limit).all()
    return db.query(tax_models.TaxDue).offset(skip).limit(limit).all()

async def get_pending_dues(db: Session, skip: int = 0, limit: int =100,uuid: str=None):
    if uuid:
        return db.query(tax_models.TaxDue).filter(tax_models.TaxDue.uuid == uuid, tax_models.TaxDue.status=='new').offset(skip).limit(limit).all()
    return db.query(tax_models.TaxDue).filter(tax_models.TaxDue.status=='new').offset(skip).limit(limit).all()