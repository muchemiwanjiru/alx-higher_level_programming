-- list all shows and genres
SELECT Ts.title, Tg.name
FROM tv_shows Ts
LEFT JOIN tv_show_genres Tsg
ON Ts.id = Tsg.show_id
LEFT JOIN tv_genres Tg
ON Tsg.genre_id = Tg.id
ORDER BY Ts.title, Tg.name;
