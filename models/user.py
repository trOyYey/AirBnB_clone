#!/usr/bin/python3
""" user class module """
from models.base_model import BaseModel


class User(BaseModel):
    """User Class.

    Attributes:
        email (str): User Email.
        password (str): User Password.
        first_name (str): User First Name.
        last_name (str): User Last Name.
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
