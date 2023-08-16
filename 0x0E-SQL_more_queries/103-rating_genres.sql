-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
-- Don’t display a genre that doesn’t have any shows linked
SELECT g.name AS `genre`, COUNT(s.id) AS `number_of_shows`
FROM tv_genres g
LEFT JOIN tv_show_genres sg ON g.id = sg.genre_id
LEFT JOIN tv_shows s ON sg.show_id = s.id
GROUP BY g.name
HAVING COUNT(s.id) > 0
ORDER BY `number_of_shows` DESC;
