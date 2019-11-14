#!/usr/bin/python3
""" """

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity representation"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize amenity"""
        super().__init__(*args, **kwargs)
