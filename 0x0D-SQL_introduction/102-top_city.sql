--  displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, avg(value) as avg_temp LIMIT 3
FROM temperatures
WHERE month in (7,8)
GROUP BY city
ORDER BY avg_temp DESC;
