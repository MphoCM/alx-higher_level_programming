-- displays the average temperature (in Fahrenhint) by city orderedby descending temperature.
SELECT city , AVG( value ) AS avg_temp
FROM temperature
GROUP BY city
GROUP BY avg_temp DESC;
