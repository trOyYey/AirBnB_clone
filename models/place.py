#!/usr/bin/python3
"""place class"""
from models.base_model import BaseModel
from typing import List


class Place(BaseModel):
    """
    city_id: string - empty string: it will be the City.id
    user_id: string - empty string: it will be the User.id
    name: string - empty string
    description: string - empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string"""
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: int = 0
    longitude: int = 0
    amenity_ids: List[str] = []
