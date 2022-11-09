from fastapi import FastAPI
from databases import Database
from app.core.config import settings
import logging

logger = logging.getLogger(__name__)


class PostgresManager:

    database = Database(settings.POSTGRES_URL)

    async def connect_to_db(self) -> None:
        # these can be configured in config as well
        try:
            await self.database.connect()
            logger.warn("DB Connection Established")
            # app.state._db = database
        except Exception as e:
            logger.warn("--- DB CONNECTION ERROR ---")
            logger.warn(e)
            logger.warn("--- DB CONNECTION ERROR ---")

    async def close_db_connection(self) -> None:
        try:
            await self.database.disconnect()
            logger.info("DB Connection Closed")
        except Exception as e:
            logger.warn("--- DB DISCONNECT ERROR ---")
            logger.warn(e)
            logger.warn("--- DB DISCONNECT ERROR ---")
