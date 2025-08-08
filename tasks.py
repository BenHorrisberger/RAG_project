from invoke import task
import pandas as pd
import sqlite3
import os

from apps.csv_to_sql import load_data

@task
def load_csv(c, csv_path="Aircraft_data/Aircraft.csv", table_name="aircraft", db_path="SQL_db/Aircraft_database.db"):
   
    pd_data_frame = pd.read_csv(csv_path)
    db_connection = sqlite3.connect(db_path)
    pd_data_frame.to_sql(table_name, db_connection, if_exists="replace", index=False)
    db_connection.close()
    print(f"loaded {csv_path} into table \'{table_name}\'")
