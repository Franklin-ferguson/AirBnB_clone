#!/usr/bin/python3
"""
module for User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents the class User
    """

    email = ""
    password =""
    first_name = ""
    last_name = ""

