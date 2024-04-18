-- CTE, UNION ALL, GROUP BY, ORDER BY, LIMIT, COUNT, DESC
WITH user_friends_count AS (
    SELECT requester_id AS user_id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS user_id
    FROM RequestAccepted
)

SELECT user_id AS id, COUNT(user_id) AS num
FROM user_friends_count
GROUP BY user_id
ORDER BY num DESC
LIMIT 1