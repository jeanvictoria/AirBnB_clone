#!/usr/bin/python3
"""class that inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """State representation"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize state"""
        super().__init__(*args, **kwargs)
