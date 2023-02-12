 CREATE OR REPLACE EXTERNAL TABLE `de-zoomcamp-3756212.trips_data_all.fhv_tripdata`
 OPTIONS (
   format = 'CSV',
   uris = ['gs://dtc_data_lake_de-zoomcamp-3756212/fhv_tripdata_2019-*.csv']
 );

 CREATE OR REPLACE TABLE `de-zoomcamp-3756212.trips_data_all.fhv_tripdata_nonpartitioned`
 AS SELECT * FROM `de-zoomcamp-3756212.trips_data_all.fhv_tripdata`;



 SELECT * FROM `de-zoomcamp-3756212.trips_data_all.fhv_tripdata` LIMIT 100

q1
 SELECT count(*) FROM `de-zoomcamp-3756212.trips_data_all.fhv_tripdata`; -- 43244696

q2
 SELECT COUNT(DISTINCT(affiliated_base_number)) FROM `de-zoomcamp-3756212.trips_data_all.fhv_tripdata`; -- 0
 SELECT COUNT(DISTINCT(affiliated_base_number)) FROM `de-zoomcamp-3756212.trips_data_all.fhv_tripdata_nonpartitioned`; -- 317MB

q3
 How many records have both a blank (null) PUlocationID and DOlocationID in the entire dataset?
 SELECT count(*)
 FROM `de-zoomcamp-3756212.trips_data_all.fhv_tripdata_nonpartitioned`
 WHERE PUlocationID IS NULL AND DOlocationID IS NULL;
 717748

q4
 What is the best strategy to optimize the table if query always filter by pickup_datetime and order by affiliated_base_number?
 Partition by pickup_datetime Cluster on affiliated_base_number

 q5
 Implement the optimized solution you chose for question 4. Write a query to retrieve the distinct affiliated_base_number between pickup_datetime 2019/03/01 and 2019/03/31 (inclusive).
 Use the BQ table you created earlier in your from clause and note the estimated bytes. Now change the table in the from clause to the partitioned table you created for question 4 and note the estimated bytes processed. What are these values? Choose the answer which most closely matches.
 CREATE OR REPLACE TABLE `de-zoomcamp-3756212.trips_data_all.fhv_tripdata_partitioned`
 PARTITION BY DATE(pickup_datetime)
 CLUSTER BY Affiliated_base_number
 OPTIONS (partition_expiration_days = 3000)
 AS
   SELECT * FROM `de-zoomcamp-3756212.trips_data_all.fhv_tripdata_nonpartitioned`
 ;

 SELECT COUNT(DISTINCT(affiliated_base_number))
 FROM  `de-zoomcamp-3756212.trips_data_all.fhv_tripdata_partitioned`
 WHERE DATE(pickup_datetime) BETWEEN '2019-03-01' AND '2019-03-31'; -- 23

 SELECT COUNT(DISTINCT(affiliated_base_number))
 FROM  `de-zoomcamp-3756212.trips_data_all.fhv_tripdata_nonpartitioned`
 WHERE DATE(pickup_datetime) BETWEEN '2019-03-01' AND '2019-03-31'; --647
