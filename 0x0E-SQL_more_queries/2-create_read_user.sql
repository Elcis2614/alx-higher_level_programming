-- Creates the data base hbtn_0d_2 and the USER user_0d_2
-- the user user_0d_2 has only the SELECT privilege in the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
DROP USER IF EXISTS 'user_0d_2_pwd'@'localhost';
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
