-- This script lists all records from the second_table that have a name value,
-- displaying the score and name, sorted by descending score.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
