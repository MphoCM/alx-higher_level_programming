-- script lists all comedy shows
SELECT ts.title FROM tv_shows AS ts
JOIN tv_show_genre AS tgs
ON ts.id = tgs.show_id
JOIN tv_gengres AS tgg
ON tgs.genre_id = tgg.id
WHERE tg.name = COMEDY'
GROUP BY ts.title ASC;
