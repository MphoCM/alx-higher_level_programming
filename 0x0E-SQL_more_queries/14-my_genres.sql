-- script uses database to list
-- all genres of the show 'Dexter'
SELECT tgg.name FROM tv_genre AS tgg
JOIN tv_genres AS tgs
ON tgs.genre_id = tgg.id
JOIN tv_shows as ts
ON ts.id = tgs.show_id
WHERE ts.title = DEXTER'
GROUP BY tgg.name ASC;
