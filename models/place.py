#!/usr/bin/python3
"""class that inherits from BaseModel"""

from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longuitude = 0.0
    amenity_ids = []

    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)
