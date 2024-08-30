WITH RECURSIVE CTE AS (
    SELECT ID, PARENT_ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    UNION ALL
    SELECT e.ID, e.PARENT_ID, CTE.GENERATION + 1
    FROM ECOLI_DATA e INNER JOIN CTE
    ON CTE.ID = e.PARENT_ID
)

SELECT COUNT(*) AS COUNT, GENERATION
FROM CTE
WHERE ID NOT IN (SELECT PARENT_ID FROM ECOLI_DATA WHERE PARENT_ID IS NOT NULL)
GROUP BY GENERATION
ORDER BY GENERATION