-- lists all records with a score >= 10 in the table second_table
-- data base name shall be pass as an argument
SELECT score, name 
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
