-- 100-move_to_utf8.sql

-- converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
ALTER DATABASE CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table
CHANGE name name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
