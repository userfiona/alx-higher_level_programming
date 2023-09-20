-- Lists all the cities of California that can be found in the database hbtn_0d_usa
-- Using a subquery to retrieve the state ID of 'California'
-- Lists all rows of a column in a database

-- Select city ID and name from the 'cities' table
-- Filter cities based on the state ID obtained from the subquery
SELECT id, name
-- From the 'cities' table
FROM cities
-- Filter cities based on the state ID of 'California'
-- Retrieved using a subquery to find the state ID from the 'states' table
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
-- Order the results by city ID in ascending order
ORDER BY id ASC;
