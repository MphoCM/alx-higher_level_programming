-- script displays the average temperature
-- by city ordered by descending temp
SELECT city, AVG(value) AS avg_temp
FROM temperature
GROUP BY city
ORDER BY avg_temp DESC;
