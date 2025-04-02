from pydantic import  BaseModel
from uuid import  UUID, uuid4
from typing import  Optional

class MenuItem(BaseModel):
    id: Optional[UUID] = None
    name : str
    description: Optional[str] = None
    price: float
    category: str #appetiser, main course, dessert
    is_available: bool = True

    class Config:
        schema_extra = {
            "example": {
                "name": "Margherita Pizza",
                "description": "Classic tomato and mozzarella",
                "price": 12.99,
                "category": "Main Course"
            }
        }




