-- RANK, ORDER BY, NULLIF
WITH cte AS (
    SELECT
        city,
        population / NULLIF(area, 0) AS density,
        RANK() OVER (ORDER BY population / NULLIF(area, 0) DESC) rank
    FROM
        cities_population
    WHERE
        area > 0
)
SELECT
    t.city,
    t.density
FROM
    cte t
WHERE
    t.rank = (SELECT MIN(rank) FROM cte)
    OR t.rank = (SELECT MAX(rank) FROM cte);