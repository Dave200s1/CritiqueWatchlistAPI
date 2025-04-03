from pydantic import BaseModel, json
from typing import Optional

class MovieUpdate(BaseModel):
    title:str
    year: int
    genre: str
    watched: bool = False
    rating: Optional[float] = None

    class Config:
        json.schema_extra = {
            'example': {
                'title': 'updated title',
                'year':2015,
                'genre': 'updated genre',
                'watched': True,
                'rating': 8.0
            }
        }