-- List all shows without genre 'Comedy' in 'hbtn_0d_tvshows'
SELECT s.title
FROM tv_shows s
LEFT JOIN tv_show_genres m ON s.id = m.show_id
LEFT JOIN tv_genres g ON m.genre_id = g.id AND g.name = 'Comedy'
WHERE g.id IS NULL
ORDER BY s.title ASC;
