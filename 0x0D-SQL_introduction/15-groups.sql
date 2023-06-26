-- lists the number of records with the same score in the table second_table
-- Database name given as an argument
SELECT score, count(score) as nummber
FROM second_table
GROUP BY score
ORDER BY score DESC;
