-- creates the table unique_id on your MySQL server and is unique
-- The database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE (id));
