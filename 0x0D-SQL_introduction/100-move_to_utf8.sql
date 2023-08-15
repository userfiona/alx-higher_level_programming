-- 100-move_to_utf8.sql

-- Converts the hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Converts the first_table table to UTF8
ALTER TABLE `hbtn_0c_0`.`first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Changes the character set and collation of the name field in first_table
ALTER TABLE `hbtn_0c_0`.`first_table`
CHANGE `name` `name` VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
