
SELECT author_id, COUNT(*) AS num_books
FROM authors
GROUP BY author_id;
