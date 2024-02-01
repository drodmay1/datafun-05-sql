-- Create authors table
CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);

-- Create books table with foreign key constraint
CREATE TABLE books (
    book_id TEXT PRIMARY KEY,
    title TEXT,
    year_published INTEGER,
    author_id TEXT,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- Import data from authors.csv
.mode csv
.import /Users/davidrodriguez/Documents/NWMO/datafun-05-sql/datafun-05-sql/authors.csv authors

-- Import data from books.csv
.import /Users/davidrodriguez/Documents/NWMO/datafun-05-sql/datafun-05-sql/books.csv books
