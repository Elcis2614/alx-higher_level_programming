-- creates a table second_table in the database and add multiples rows
-- data base name shall be pass as an argument
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT );
INSERT INTO second_table
VALUES (10, "Paul", 19),
(24, NULL, 3);
