-- Lists all shows from hbtn_0d_tvshows that have at least one genre linked.
-- Select the title of shows and the corresponding genre_id from linked genres
SELECT s.title, g.genre_id
-- Specify the tables to retrieve data from
FROM tv_shows s
-- Inner join to link shows with their associated genres
INNER JOIN tv_show_genres g
ON s.id = g.show_id
-- Order the results by show title and genre ID in ascending order
ORDER BY s.title ASC, g.genre_id ASC;
