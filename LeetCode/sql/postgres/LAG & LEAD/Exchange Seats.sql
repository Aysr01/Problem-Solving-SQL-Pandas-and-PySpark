-- CASE, WHEN, LAG, LEAD, IS NOT NULL, WINDOW FUNCTION
SELECT
    id,
    CASE
        WHEN id % 2 = 0 THEN LAG(student) OVER()
        WHEN LEAD(student) OVER() IS NOT NULL THEN LEAD(student) OVER()
        ELSE student
    END AS student
FROM
    Seat