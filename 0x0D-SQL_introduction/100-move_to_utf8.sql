-- converts hbtn_0c_0 database to UTF8
-- The database name will be passed as an argument
ALTER DATABASE EXOS CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
