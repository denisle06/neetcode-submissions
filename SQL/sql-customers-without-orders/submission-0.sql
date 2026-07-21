-- Write your query below
SELECT name FROM customers 
WHERE NOT EXISTS(
    SELECT customer_id FROM orders WHERE orders.customer_id = customers.id
)
    
