#!/usr/bin/python3
"""review class that enhirits form BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review class"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
