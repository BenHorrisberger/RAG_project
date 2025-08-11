import sqlite3
from pathlib import Path

from .aircraft_class import Aircraft

DB_PATH = Path(__file__).parent.parent / "Database" / "Aircraft_database.db"

def get_connection():
    connection_db = sqlite3.connect(DB_PATH)
    connection_db.row_factory = sqlite3.Row
    return connection_db

def query_database(total_seats:int=0, num_bags:int=0, fuel_stop_distance:int=0):

    connection_db = get_connection()
    cursor_db = connection_db.cursor()

    query = "SELECT * FROM aircraft WHERE total_seats >= ? AND num_bags >= ? AND fuel_stop_distance >= ?"

    cursor_db.execute(query, (total_seats, num_bags, fuel_stop_distance))
    records = cursor_db.fetchall()
    connection_db.close()

    return [Aircraft(**dict(record)) for record in records]
