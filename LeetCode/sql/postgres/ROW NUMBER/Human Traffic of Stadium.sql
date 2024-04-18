-- CTE, ROW_NUMBER, GROUP BY, HAVING, WHERE, IN, COUNT, WINDOW FUNCTION
WITH cte AS(
    SELECT 
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER() as lt_100_count
        -- The field above counts the number of rows where the number of visitors
        -- is less than 100
    FROM Stadium
    WHERE people >= 100
)

SELECT
    id,
    visit_date,
    people
FROM cte
WHERE lt_100_count IN (
    SELECT lt_100_count
    FROM cte
    GROUP BY lt_100_count
    HAVING COUNT(lt_100_count) >= 3
)