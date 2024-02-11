#!/usr/bin/python3
"""amenity class that enhirites from BaseModel"""
from base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name: str = ""
    pass
