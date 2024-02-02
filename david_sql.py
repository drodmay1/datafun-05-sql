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
import csv
import uuid

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")


def create_database(db_file):
    """Function to create an SQLite database file."""
    try:
        with sqlite3.connect(db_file) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS authors (
                    author_id INTEGER PRIMARY KEY,
                    author_name TEXT
                )
            """)
            
            conn.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY,
                    title TEXT,
                    author_id INTEGER,
                    FOREIGN KEY (author_id) REFERENCES authors(author_id)
                )
            """)
            
            print("Database created successfully.")
    except sqlite3.Error as e:
        print("Error creating database:", e)

def insert_data_from_csv(db_file):
    """Function to use pandas to read data from CSV files (in 'data' folder)
    and insert the records into their respective tables."""
    try:
        create_database(db_file)  # Create the database

        author_data_path = Path("data", "authors.csv")
        book_data_path = Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)

        with sqlite3.connect(db_file) as conn:
            # Use the pandas DataFrame to_sql() method to insert data
            # Pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace" if authors_df.empty else "append", index=False)
            books_df.to_sql("books", conn, if_exists="replace" if books_df.empty else "append", index=False)

            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data:", e)

# Insert data from CSV
insert_data_from_csv("book_db.db")

git add .
git commit -m "Add CSV files"
git push origin main  # or the name of your branch

