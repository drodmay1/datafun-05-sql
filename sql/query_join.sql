-- Perform INNER JOIN operation between authors and books tables
SELECT authors.author_id, authors.first, authors.last, books.book_id, books.title, books.year_published
FROM authors
INNER JOIN books ON authors.author_id = books.author_id;
