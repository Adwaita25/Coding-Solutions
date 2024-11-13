# Write your MySQL query statement below
SELECT 
    ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM delivery 
WHERE (customer_id, order_date) IN 
    (SELECT customer_id, MIN(order_date) AS first_order
    FROM delivery
    GROUP BY customer_id)
