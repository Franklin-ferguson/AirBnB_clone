#!/usr/bin/python3
"""Review"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Represents a class State inherited from BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""
