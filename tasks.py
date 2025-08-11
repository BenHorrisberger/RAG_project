from invoke import task
import pandas as pd
import sqlite3

@task(help={

    "csv_path":"Path from project root to .csv file, default=Aircraft_data/Aircraft",
    "table_name":"name for the SQL table being created or rewritten, defualt=aircraft",
    "db_path":"Path from project root to sqlite3 database, defualt=Database/Aircraft_database"
})
def load_csv(c, csv_path="Aircraft_data/Aircraft.csv", table_name="aircraft", db_path="Database/Aircraft_database.db"):
    """Load .csv file into sqlite3 database""" 
    pd_data_frame = pd.read_csv(csv_path)
    db_connection = sqlite3.connect(db_path)
    pd_data_frame.to_sql(table_name, db_connection, if_exists="replace", index=False)
    db_connection.close()
    print(f"loaded {csv_path} into table \'{table_name}\'")
