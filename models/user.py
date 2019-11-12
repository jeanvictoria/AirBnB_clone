#!/usr/bin/python3
"""class that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """User representation """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User"""
        super().__init__(*args, **kwargs)
