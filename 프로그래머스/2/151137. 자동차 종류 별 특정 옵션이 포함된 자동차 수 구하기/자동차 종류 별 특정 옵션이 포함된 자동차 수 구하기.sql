SELECT CAR_TYPE, count(*) AS CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE options like '%시트%'
GROUP BY car_type
ORDER BY car_type;