SELECT id,actual, 
    (SELECT SUM(actual) 
        FROM target_actual b 
        WHERE b.id <= a.id) AS b 
FROM target_actual a