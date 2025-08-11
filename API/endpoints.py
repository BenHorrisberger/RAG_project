from fastapi import APIRouter, Query
from typing import List

from .database import get_connection, query_database
from .aircraft_class import Aircraft
from .openai_model import prompt_to_query

router = APIRouter()

# base home page
@router.get("/")
def base_page():
    return {"messge" : "welcome to aircraft_api"}

# query method
@router.get("/aircraft/query", response_model=List[Aircraft])
def query(
    total_seats:int = Query(0, description="Required number of seats"),
    num_bags:int = Query(0, description="Required number of bags"),
    fuel_stop_distance:int = Query(0, description="Required aircraft range"),
    ):
    
    return query_database(total_seats, num_bags, fuel_stop_distance)

@router.get("/chat")
def chat(prompt:str):
    json_response =  prompt_to_query(prompt)
    
    if "error" in json_response:
        return result

    total_seats = json_response.get("total_seats", 0)
    num_bags = json_response.get("num_bags", 0)
    fuel_stop_distance = json_response.get("fuel_stop_distance", 0)

    return query_database(total_seats, num_bags, fuel_stop_distance)
