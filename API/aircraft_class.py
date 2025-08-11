from typing import Optional
from pydantic import BaseModel

class Aircraft(BaseModel):
    id : Optional[int]
    manufacturer : Optional[str]
    aircraft_make : Optional[str]
    aircraft_model : Optional[str]
    aircraft_variant : Optional[str]
    full_aircraft_type : Optional[str]
    category_name : Optional[str]
    total_seats : Optional[int]
    cabin_dimensions_height : Optional[int]
    cabin_dimensions_width : Optional[int]
    cabin_dimensions_length : Optional[int]
    baggage_capacity : Optional[int]
    num_bags : Optional[int]
    cruise_speed : Optional[int]
    max_range : Optional[int]
    fuel_stop_distance : Optional[int]
    fuel_stop_hours : Optional[float]
