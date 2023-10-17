#!/usr/bin/python3
"""Defines the user class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user.

    Attributes:
        email (str): The email of the user.
        password (str): Password of the user.
        first_name (str): first name of the user.
        last_name (str): last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
