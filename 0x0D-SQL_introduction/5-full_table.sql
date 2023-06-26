-- gives description of the table first_table
-- Database name given as an argument
-- SHOW FULL COLUMNS FROM first_table;

SELECT CCSA.character_set_name FROM information_schema.`TABLES` T,information_schema.`COLLATION_CHARACTER_SET_APPLICABILITY` CCSA WHERE CCSA.collation_name = T.table_collation AND T.table_schema = "EXOS" AND T.table_name = "first_table";
