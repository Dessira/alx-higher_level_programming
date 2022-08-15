-- Lists the number of records with the same score in the table
-- Displays the score, number
-- Sorted descending order
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
