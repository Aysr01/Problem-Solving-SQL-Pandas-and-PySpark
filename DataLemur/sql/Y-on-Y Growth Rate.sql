-- CTE, LAG, OVER, PARTITION BY, ORDER BY, EXTRACT, ROUND, CASE
-- This query calculates the year-on-year growth rate for each product based on the spend amount for the current year and the previous year.
-- The query uses the LAG window function to get the previous year's spend amount for each product and then calculates the growth rate as
-- the percentage change from the previous year to the current year. The result includes the product ID, current year spend amount,
-- previous year spend amount, and year-on-year growth rate for each product.

WITH previous_year_spend AS (
  SELECT EXTRACT('year' FROM transaction_date),
      product_id,
      spend as curr_year_spend,
      LAG(spend) OVER(PARTITION BY product_id ORDER BY transaction_date asc) as prev_year_spend
  FROM user_transactions
)

SELECT *,
  CASE
    WHEN prev_year_spend IS NOT NULL THEN ROUND((curr_year_spend - prev_year_spend) / prev_year_spend * 100, 2)
    ELSE NULL
  END AS yoy_rate
FROM previous_year_spend