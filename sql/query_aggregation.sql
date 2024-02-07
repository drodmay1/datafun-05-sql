-- Count the total number of authors
SELECT COUNT(*) AS total_authors
FROM authors;

-- avg year of year published in books table
SELECT AVG(year_published) AS average_publication_year
FROM books;

-- total of sum of publication years
SELECT SUM(year_published) AS total_published_years
FROM books;
