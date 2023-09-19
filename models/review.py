#!/usr/bin/python3
"""Review class defined"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Inherits from BaseModel
    Attributes:
    place_id:            (str) Assign Place.id
        user_id:             (str) Assign User.id
        text:                (str)
    """
    place_id = ""
    user_id = ""
    text = ""
