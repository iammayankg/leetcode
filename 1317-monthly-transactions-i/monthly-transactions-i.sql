# Write your MySQL query statement below
SELECT
LEFT(trans_date, 7) as month,
country,
COUNT(*) as trans_count,
SUM(state = "approved") as approved_count,
SUM(amount) as trans_total_amount,
SUM((state="approved") * amount) as approved_total_amount
FROM
Transactions
GROUP BY
month,
country