-- script that lists all shows contained in the database hbtn_0d_tvshows.
-- Select the title of shows and the corresponding genre_id (if any)
SELECT tv_shows.title, tv_show_genres.genre_id
-- Specify the table to retrieve data from
FROM tv_shows
-- Left join to link shows with their associated genres
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Order the results by show title and genre ID in ascending order
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
