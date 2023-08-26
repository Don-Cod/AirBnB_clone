#!/usr/bin/python3
"""Place class defined"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents the place
    Public class attributes:
        city_id:             (str)  City.id
        user_id:             (str)  User.id
        name:                (str)
        description:         (str)
        number_rooms:        (int) 0
        number_bathrooms:    (int) 0
        max_guest:           (int) 0
        price_by_night:      (int) 0
        latitude:            (float) 0.0 Latitude of the place
        longitude:           (float) 0.0 Longitude of the place
        amenity_ids:         (list) Amenity.id
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
