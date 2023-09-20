-- Lists all cities contained in the database hbtn_0d_usa
-- Each record should display: cities.id - cities.name - states.name
-- Results must be sorted in ascending order by cities.id
-- You can use only one SELECT statement

-- Select the city ID, city name, and state name
-- Using a comma-separated table list for implicit cross join
SELECT c.id, c.name, s.name
-- Specify the tables to retrieve data from
FROM cities AS c, states AS s
-- Apply the condition to link city to state
WHERE c.state_id = s.id
-- Order the results by city ID in ascending order
ORDER BY c.id ASC;
