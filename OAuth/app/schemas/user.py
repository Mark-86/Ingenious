from typing import Any, Dict, List, Optional
from pydantic import BaseModel, root_validator
import datetime


class UpdateRole(BaseModel):
    email: str
    old_role: str
    new_role: str


class TaxPayersReq(BaseModel):
    page: int = 1
    per_page: int = 10
