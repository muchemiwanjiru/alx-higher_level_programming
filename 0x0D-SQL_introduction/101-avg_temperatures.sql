-- a script that displays the average temperature (Fahrenheit) 
-- is a city ordered by temp
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
