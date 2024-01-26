-- Active: 1706226636448@@127.0.0.1@5432@taxi_dataset@public
-- Active: 1706226636448@@127.0.0.1@5432@taxi_dataset@public

-- How many taxi trips were totally made on September 18th 2019?
SELECT count(*)
FROM taxi_trips
WHERE DATE(lpep_pickup_datetime) = DATE(lpep_dropoff_datetime) AND DATE(lpep_pickup_datetime) = '2019-09-18';

-- Which was the pick up day with the largest trip distance Use the pick up time for your calculations.
select DATE(lpep_pickup_datetime),MAX(trip_distance) from taxi_trips
group by 1
order by 2 desc
LIMIT 1;

-- Consider lpep_pickup_datetime in '2019-09-18' and ignoring Borough has Unknown

-- Which were the 3 pick up Boroughs that had a sum of total_amount superior to 50000?
SELECT z."Borough", SUM(t."total_amount")
FROM taxi_trips t JOIN zones z
    ON t."PULocationID" = z."LocationID"

WHERE DATE(t."lpep_pickup_datetime") = '2019-09-18'
GROUP BY 1
HAVING SUM(t."total_amount") > 50000
ORDER BY 2
LIMIT 3;


-- For the passengers picked up in September 2019 in the zone name Astoria which was the drop off zone that had the largest tip? We want the name of the zone, not the id.
WITH the_condition AS(
    SELECT *
    FROM taxi_trips t JOIN zones z
      ON t."PULocationID" = z."LocationID"
    WHERE DATE_TRUNC('month', t.lpep_pickup_datetime) = '2019-09-01'
    AND z."Zone" = 'Astoria'
)

SELECT "Zone" FROM zones
WHERE "LocationID" = (
    SELECT "DOLocationID"
    FROM (
        SELECT "DOLocationID", MAX(tip_amount)
        FROM the_condition
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 1
    ) sub
);


