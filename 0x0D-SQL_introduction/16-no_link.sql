-- This script lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server
-- It doesn't list rows without a name value
-- Results display the score and the name (in this order)
-- Records are listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
-- End of script
