SELECT i.NAME, i.DATETIME
FROM ANIMAL_INS i LEFT OUTER JOIN ANIMAL_OUTS o
ON i.ANIMAL_ID = o.ANIMAL_ID
WHERE i.ANIMAL_ID NOT IN (SELECT ANIMAL_ID FROM ANIMAL_OUTS)
ORDER BY i.DATETIME
LIMIT 3;