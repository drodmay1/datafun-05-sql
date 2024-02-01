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
connection = sqlite3.connect('books.db')
pd.options.display.max_columns = 10
pd.read_sql('SELECT * FROM authors', connection,
            index_col=['id'])
