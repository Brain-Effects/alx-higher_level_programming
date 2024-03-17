-- Select the id of California from the states table
SET @california_id = (SELECT id FROM states WHERE name = 'California');

-- Select all cities in California from the cities table
SELECT id, name FROM cities WHERE state_id = @california_id ORDER BY id ASC;
