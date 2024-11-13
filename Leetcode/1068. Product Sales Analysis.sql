SELECT p.product_name, s.year, s.price
FROM Sales s
LEFT JOIN Product p
ON S.product_id = p.product_id
