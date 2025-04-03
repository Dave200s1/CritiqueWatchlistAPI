from pydantic import BaseModel, json
from typing import Optional

class MovieCreate(BaseModel):
    title:str
    year: int
    genre: str
    watched: bool = False
    rating: Optional[float] = None

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'Minions',
                'year':2015,
                'genre': 'Animation',
                'watched': True,
                'rating': 8.0
            }
        }
