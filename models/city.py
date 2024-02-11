#!/usr/bin/python3
"""city class that enhirites from BaseModel"""
from base_model import BaseModel


class city(BaseModel):
    """city class"""

    state_id: str = ""
    name: str = ""
    pass
