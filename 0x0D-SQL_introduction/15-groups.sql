-- 15-groups.sql

-- Prints the number of records within a group in the table in the database
SELECT `score`, COUNT(`score`) AS `number`
FROM `hbtn_0c_0`.`second_table`
GROUP BY `score`
ORDER BY `number` DESC;
