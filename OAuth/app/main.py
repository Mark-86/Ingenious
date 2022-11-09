from turtle import pos
from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
import uvicorn
from app.db.postgres import PostgresManager
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.responses import JSONResponse
from app.core.config import auth_jwt_settings
from fastapi_jwt_auth import AuthJWT
from app.api import api
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)
postgres = PostgresManager()

app = FastAPI(title="GST Management APP", version="0.0.1")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():

    await postgres.connect_to_db()


@app.on_event("shutdown")
async def shutdown():
    await postgres.close_db_connection()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@AuthJWT.load_config
def get_config():
    return auth_jwt_settings


@app.get("/ping")
async def ping():
    return {"ping": "pong"}


app.include_router(api.api_router)

if __name__ == "__main__":
    uvicorn.run(
        # "backend.app.main:app",
        host="0.0.0.0",
        port=4522,
        log_level="info",
        reload=True,
        workers=1,
    )
