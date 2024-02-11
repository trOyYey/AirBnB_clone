#!/usr/bin/python3
"""city class that enhirites from BaseModel"""
from models.base_model import BaseModel


class city(BaseModel):
    """city class"""

    state_id: str = ""
    name: str = ""
