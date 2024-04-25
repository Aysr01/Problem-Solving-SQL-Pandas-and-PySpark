-- CTE, ROW NUMBER, ORDER BY, GROUP BY, COUNT, DESCs
WITH user_email_counts AS (
  SELECT
    from_user,
    COUNT(*) AS total_emails
  FROM
    google_gmail_emails
  GROUP BY
    from_user
)

SELECT
  from_user,
  total_emails,
  ROW_NUMBER() OVER (ORDER BY total_emails DESC, from_user) AS row_number
FROM
  user_email_counts