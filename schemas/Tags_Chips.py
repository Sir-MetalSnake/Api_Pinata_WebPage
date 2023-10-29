from pydantic import BaseModel
from typing import Optional


class Model_Chip(BaseModel):
    Id_Chip: Optional[int] = None
    Detail: Optional[str] = None


class Model_ChipResponse(Model_Chip):
    Id_Chip: int
