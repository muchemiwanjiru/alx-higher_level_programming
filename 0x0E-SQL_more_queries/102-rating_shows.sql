-- listing all shows from a database by their rating
SELECT Ts.title, SUM(Tsr.rate) rating
FROM tv_show_ratings Tsr, tv_shows Ts
WHERE Tsr.show_id = Ts.id
GROUP BY Ts.title
ORDER BY rating DESC;
