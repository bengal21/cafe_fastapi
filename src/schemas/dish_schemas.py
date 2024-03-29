from uuid import UUID
from typing import Optional
from pydantic import BaseModel

class DishInput(BaseModel):
    title: str
    description: str
    price: float


class DishOutput(BaseModel):
    id: UUID
    title: str
    description: str
    price: str
    submenu_id: UUID


class DishUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

