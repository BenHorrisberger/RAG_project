import pandas as pd
import sqlite3
from pathlib import Path

def load_csv_to_sql(csv_path: Path, table_name: str):
    """Load csv data into a sql database"""
    pandas_data_frame = pd.read_csv(csv_path)
    print(pandas_data_frame.head())

if __name__ == "__main__":
    pass
