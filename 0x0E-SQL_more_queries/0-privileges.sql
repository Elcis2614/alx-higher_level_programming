-- lists all privileges of the MySQL users user_0d_1 and user_0d_2 on localhost
-- If it changes anything
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
