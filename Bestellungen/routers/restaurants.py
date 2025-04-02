from fastapi import APIRouter, HTTPException
from uuid import UUID, uuid4
from typing import List
from models.restaurant import MenuItem

router = APIRouter(prefix="/restaurants", tags=["restaurants"])

# in-memory database
menu_items = []

@router.post("/menu-items/", response_model=MenuItem)
def create_menu_item(item: MenuItem):
    item.id = uuid4()
    menu_items.append(item)
    return item

@router.get("/menu-items/", response_model=List[MenuItem])
def get_all_menu_items(category: str = None):
    if category:
        return [item for item in menu_items if item.category == category]
    return menu_items

@router.get("/menu-items/{item_id}", response_model=MenuItem)
def get_menu_item(item_id: UUID):
    for item in menu_items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Menu item not found")

# ToDO Add more endpoints (update, delete, etc.)
@router.put("/menu-items/{item_id}", response_model= MenuItem)
def update_menu_item(item_id: UUID, item_update: MenuItem):
    for idx in MenuItem in enumerate(menu_items):

        if MenuItem.id == item_id:
            update_menu_item = MenuItem.copy(update=item_update.dict(exclude_unset=True))
            menu_items[idx] = update_menu_item
            return update_menu_item
        raise HTTPException (status_code= 404, detail="Item not found")
