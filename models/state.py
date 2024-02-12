#!/usr/bin/python3
"""state class that enhirts from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """state from BaseModel"""

    name: str = ""
