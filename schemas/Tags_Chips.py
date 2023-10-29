from pydantic import BaseModel
from typing import Optional


class Model_Chip(BaseModel):
    Detail: str


class Model_ChipResponse(Model_Chip):
    Id_Chip: int
