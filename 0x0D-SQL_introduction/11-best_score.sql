-- 11-best_score.sql

-- Lists all records with a score >= 10 in the table second_table of the database hbtn_0c_0
-- Results display both the score and the name (in this order)
-- Records are ordered by score (top first)

SELECT score, name
FROM `hbtn_0c_0`.`second_table`
WHERE score >= 10
ORDER BY score DESC;
