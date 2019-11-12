#!/usr/bin/python3
"""class that inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review representation"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize review"""
        super().__init__(*args, **kwargs)
