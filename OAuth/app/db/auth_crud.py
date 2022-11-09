from sqlalchemy.orm import Session
from app.schemas import auth as auth_schemas
from app.models import auth as auth_models
from uuid import uuid4


async def get_user(db: Session, uuid: str):
    return db.query(auth_models.User).filter(auth_models.User.uuid == uuid).first()


async def get_user_by_email(db: Session, email: str):
    return db.query(auth_models.User).filter(auth_models.User.email == email).first()


async def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(auth_models.User).offset(skip).limit(limit).all()


async def get_tax_payers(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(auth_models.User)
        .filter(auth_models.User.role == "taxpayer")
        .offset(skip)
        .limit(limit)
        .all()
    )


async def create_user(db: Session, user: auth_schemas.UserInDB):
    db_user = auth_models.User(
        email=user.email,
        hashed_password=user.hashed_password,
        uuid=user.uuid,
        role=user.role,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


async def get_token(db: Session, uuid: str):
    return (
        db.query(auth_models.UserTokens)
        .filter(auth_models.UserTokens.uuid == uuid)
        .first()
    )


async def create_token(db: Session, token: auth_schemas.UserTokens):

    token = auth_models.UserTokens(
        uuid=token.uuid,
        access_token=token.access_token,
        refresh_token=token.refresh_token,
    )
    db.add(token)
    db.commit()
    db.refresh(token)
    return token


async def update_refresh_and_access_token(
    db: Session, uuid: str, access_token: str, refresh_token: str
):
    token = (
        db.query(auth_models.UserTokens)
        .filter(auth_models.UserTokens.uuid == uuid)
        .first()
    )
    token.access_token = access_token
    token.refresh_token = refresh_token

    db.add(token)
    db.commit()
    db.refresh(token)
    return token
