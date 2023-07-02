-- Creates the user user_0d_1 , and grant all privileges
DROP USER IF EXISTS 'user_0d_1'@'localhost';
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED WITH BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ION *.* TO 'user_0d_1'@'localhost';
