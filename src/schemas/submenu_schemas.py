from uuid import UUID
from typing import Optional
from pydantic import BaseModel


class SubMenuInput(BaseModel):
    title: str
    description: str


class SubMenuOutput(BaseModel):
    id: UUID
    title: str
    description: str
    dishes_count: int
    menu_id: UUID


class SubMenuUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
