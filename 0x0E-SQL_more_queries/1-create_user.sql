-- Creates the user user_0d_1 , and grant all privileges
CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO 'user_0d_1' WITH GRANT OPTION;
