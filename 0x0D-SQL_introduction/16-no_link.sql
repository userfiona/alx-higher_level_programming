-- 16-no_link.sql

-- Lists all records of the table second_table having a name value in the database
-- Records are ordered by descending score.

SELECT `score`, `name`
FROM `hbtn_0c_0`.`second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
