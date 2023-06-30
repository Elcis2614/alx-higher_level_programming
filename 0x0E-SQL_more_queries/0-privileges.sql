-- lists all privileges of the MySQL users user_0d_1 and user_0d_2 on localhost
-- If it changes anything
UPDATE mysql.user SET Super_Priv='Y' WHERE user='user_0d_1' OR user='user_0d_1' AND host='localhost';
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
