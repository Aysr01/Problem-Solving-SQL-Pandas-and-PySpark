-- CTEs, CASE, DATE, GROUP BY, HAVING
WITH user_sessions AS (
  SELECT
    user_id,
    DATE(timestamp) AS session_date,
    MAX(CASE WHEN action = 'page_load' THEN timestamp END) AS load_time,
    MIN(CASE WHEN action = 'page_exit' THEN timestamp END) AS exit_time
  FROM
    facebook_web_log
  GROUP BY
    user_id, session_date
  HAVING
    MAX(CASE WHEN action = 'page_load' THEN timestamp END) < MIN(CASE WHEN action = 'page_exit' THEN timestamp END)
)
SELECT
  user_id,
  AVG((exit_time - load_time)) AS avg_session_time
FROM
  user_sessions
GROUP BY
  user_id;