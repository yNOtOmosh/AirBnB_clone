#!/usr/bin/python3
"""Defines the class Review."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Repressnts a review.

    Attributes:
        place_id (str): place id.
        user_id (str): user id.
        text (str): the text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
