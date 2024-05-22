--a script that converts hbtn_0c_0 database to UTF8 
--add into mysql server
USE `hbtn_0c_0`
ALTER TABLE `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
