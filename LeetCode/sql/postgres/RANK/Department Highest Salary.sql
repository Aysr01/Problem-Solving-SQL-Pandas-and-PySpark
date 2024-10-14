-- RANK, WHERE, WITH, SELECT, FROM, ORDER BY, PARTITION BY
-- This query returns the employee with the highest salary in each department.
WITH salaries_rank
AS (
    SELECT 
        department.name as Department,
        employee.name as Employee,
        employee.salary as Salary,
        RANK() OVER(PARTITION BY departmentId ORDER BY salary desc) as salary_rank
    FROM employee, department
    WHERE employee.departmentId = Department.id
)

SELECT Department, Employee, Salary
FROM salaries_rank
WHERE salary_rank = 1