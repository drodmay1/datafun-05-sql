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

connection = sqlite3.connect('books.db')
pd.options.display.max_columns = 10
pd.read_sql('SELECT * FROM authors', connection,
            index_col=['id'])

