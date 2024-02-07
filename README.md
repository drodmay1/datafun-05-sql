# datafun-05-sql
project 5 for 44608

## Overview
In this module, we cover SQL (structured query language), used to work with relational data - well-structured information kept in data base management systems (DBMS) or even a series of Excel spreadsheets.

## Project Stucture & Deliverables

- `Proj5_SQL_Python.py`: this is the python file
- `README.md`: Overview of P5 og 44608
- `requirements.txt`: requirement list

## Environment Setup & How to Install the Project

Created a GitHub project repository: datafun-05-sql
Cloned repo to local
Used VSCode to open project
Added a .gitignore with `.vsode/` and `.venv/` 
Created and activated a local virtual environment in `.venv.`
    - `python -m venv .venv`
    - `.\.venv\Scripts\activate`

Installed dependencies in `.venv` 
(pandas and pyarrow) and freezed in requirements.txt.
    - `pip install pandas pyarrow`
    - `pip freeze > requirements.txt`

Performed add and commit with a useful message and pushed to GitHub.
    - `git add .`
    - `git commit -m "initial commit"`
    - `git push origin main`


## Import Dependencies
```python
import sqlite3
import pandas as pd
import pathlib
```

## Logging
Implement logging to enhance debugging and maintain a record of program execution.

```python
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")
```

## Schema Design & Database Creation
 - Create new SQLite database file.

 - Design schema with at least two related tables, including foregin key constraints.


## SQL Operations
Implemented SQL statements and queries to perform table creation, data insertion, data querying (with filters, sorting, and joining tables), data aggregation, and record update and deletion.

SQL files:

1. create_tables.sql 
2. insert_records.sql
3. update_records.sql
4. delete_records.sql
5. query_aggregation.sql
6. query_filter.sql
7. query_sorting.sql
8. query_group_by.sql
9. query_join.sql

## Python and SQL Integration
Use Python to interact with the SQL with the following commands:

```python
import sqlite3

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

```

## Define Main Function
Implemented a main() function to execute the project logic.

## References & Acknowledgments
(https://openai.com/)

# macOS system files
.DS_Store
