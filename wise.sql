SELECT 
    w.address, 
    COUNT(t) AS Transactions
    SUM(t.amount) AS BALANCE
FROM 
        wallets w 
    LEFT JOIN 
        transactions t
    ON 
        w.id = t.wallet_id
    WHERE
        SUM(t.amount) > 0
    AND
        COUNT(t) > 10
GROUP BY 
    w.id 
ORDER BY SUM(t.amount) DESC;