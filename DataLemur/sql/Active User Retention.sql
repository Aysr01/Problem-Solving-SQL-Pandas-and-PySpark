-- WITH, LAG, EXTRACT, date_trunc, interval, count, distinct, GROUP BY
-- This query calculates the number of users who performed an action in two consecutive months.
WITH user_consecutive_events AS (
  SELECT
    user_id,
    event_date,
    LAG(event_date) OVER(PARTITION BY user_id ORDER BY event_date asc) as previous_date
  FROM user_actions
)

SELECT EXTRACT('month' from event_date), count(distinct user_id)
FROM user_consecutive_events
WHERE date_trunc('month', event_date) - date_trunc('month', previous_date) = interval '1 month'
GROUP BY EXTRACT('month' from event_date);