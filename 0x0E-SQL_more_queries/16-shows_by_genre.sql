-- script lists all shows and genres
-- linked to a show
SELECT ts.title, tgg.name FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tgs
ON ts.id = tgs.show_id
LEFT JOIN tv-genres AS tgg
ON tgs.genre_id = tgg.id
ORDER BY ts.title, tgg.name;
