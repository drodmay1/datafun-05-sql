import sqlite3
import pandas as pd
connection = sqlite3.connect('books.db')
pd.options.display.max_columns = 10
pd.read_sql('SELECT * FROM authors', connection,
            index_col=['id'])
