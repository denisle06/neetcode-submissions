-- Write your query below
SELECT s.seller_name
FROM Seller s
LEFT JOIN Orders o
       ON s.seller_id = o.seller_id
      -- Filter in the JOIN, not WHERE: rows for 2020 orders must be
      -- discarded *before* the outer join decides what's unmatched.
      -- Putting this in WHERE would drop the NULL rows we're looking for.
      AND EXTRACT(YEAR FROM o.sale_date) = 2020
WHERE o.seller_id IS NULL   -- no surviving 2020 order => seller had none
ORDER BY s.seller_name ASC;