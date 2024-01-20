-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT name
from tv_show_genres
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE title = "Dexter"
ORDER BY name ASC;
