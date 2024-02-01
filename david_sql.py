"""
Project for Module 5 Learn databases and SQL

This project ntegrates Python and SQL, focusing on database interactions using SQLite.
introduces logging, creating and managing databases and SQL operations
ncluding queries with joins, filters, and aggregations.

Author: David Rodriguez Mayorquin
Date: 2/1/2024

Dependencies:
Pandas
Pyarrow
"""


import sqlite3
import pandas as pd
from pathlib import Path
import logging
import sqlite3

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")

