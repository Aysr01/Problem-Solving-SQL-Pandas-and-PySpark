-- CTE, CASE, FLOOR, ORDER BY
WITH density AS (
    SELECT
        city,
        country,
        CASE
            WHEN area > 0 THEN FLOOR(population / area)
            ELSE 0
        END AS density
    FROM cities_population
    WHERE area>0
)
SELECT d.city, d.country, d.density
FROM density d
WHERE d.density IN (
    (SELECT MIN(density) FROM density),
    (SELECT MAX(density) FROM density)
)
ORDER BY density;