"""
Project for Module 5 Learn databases and SQL

This project integrates Python and SQL, focusing on database interactions using SQLite.
introduces logging, creating and managing databases and SQL operations
including queries with joins, filters, and aggregations.

Author: David Rodriguez Mayorquin
Date: 2/6/2024

Dependencies:
Pandas
Pyarrow
"""

import sqlite3
import pandas as pd
import pathlib
import logging
import matplotlib
import csv
import uuid
import pyarrow

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

def main():
    db_filepath = '/Users/davidrodriguez/Documents/NWMO/datafun-05-sql/datafun-05-sql/project.db'

    # Create database schema and populate with data
    execute_sql_from_file(db_filepath, 'sql/create_tables.sql')
    execute_sql_from_file(db_filepath, 'sql/insert_records.sql')
    execute_sql_from_file(db_filepath, 'sql/update_records.sql')
    execute_sql_from_file(db_filepath, 'sql/delete_records.sql')
    execute_sql_from_file(db_filepath, 'sql/query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'sql/query_filter.sql')
    execute_sql_from_file(db_filepath, 'sql/query_sorting.sql')
    execute_sql_from_file(db_filepath, 'sql/query_group_by.sql')
    execute_sql_from_file(db_filepath, 'sql/query_join.sql')

    logging.info("All SQL operations completed successfully")

if __name__ == "__main__":
    main()

