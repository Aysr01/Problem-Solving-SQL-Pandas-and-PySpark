-- CTE, RANK, JOIN, WHERE
WITH indexed_sales AS(
    SELECT 
        product_id,
        year,
        quantity,
        price,
        RANK() OVER(partition by product_id order by year asc) as rk
    FROM Sales
)

SELECT 
    i.product_id,
    year as first_year,
    quantity,
    price
FROM indexed_sales i
JOIN Product p
ON i.product_id = p.product_id
WHERE rk = 1
