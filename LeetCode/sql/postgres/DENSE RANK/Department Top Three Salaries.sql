-- DENSE RANK, PARTITION BY, ORDER BY, DESC, JOIN, WHERE
SELECT Department, employee, salary FROM (
    SELECT 
        d.name AS Department,
        e.name AS employee,
        e.salary,
        DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS dense_rank
    FROM Employee e JOIN Department d ON e.DepartmentId= d.Id
)
WHERE dense_rank <= 3;