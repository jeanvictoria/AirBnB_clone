#!/usr/bin/python3
""" """

from models.base_model import BaseModel


class City(BaseModel):
    """City representation"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize city"""
        super().__init__(*args, **kwargs)
