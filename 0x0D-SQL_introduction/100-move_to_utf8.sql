-- converts hbtn_0c_0 database to UTF8
-- The database name will be passed as an argument
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE CHANGE name VARCHAR(256) CHARACTER SET uft8mb4 COLLATE utf8mb4_unicode_ci;
