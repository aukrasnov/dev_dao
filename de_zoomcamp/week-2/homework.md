```
cd week-1/terraform
terraform apply
```

Question 1. Load January 2020 data
Using the etl_web_to_gcs.py flow that loads taxi data into GCS as a guide, create a flow that loads the green taxi CSV dataset for January 2020 into GCS and run it. Look at the logs to find out how many rows the dataset has.

How many rows does that dataset have?

- 447,770
- 766,792
- 299,234
- 822,132

ANSWER: 447770

``
23:51:59.924 | INFO    | Task run 'clean-b9fd7e03-0' - rows: 447770
``


Question 2. 0 5 1 * *

Question 3. Loading data to BigQuery
Using etl_gcs_to_bq.py as a starting point, modify the script for extracting data from GCS and loading it into BigQuery. This new script should not fill or remove rows with missing values. (The script is really just doing the E and L parts of ETL).
The main flow should print the total number of rows processed by the script. Set the flow decorator to log the print statement.
Parametrize the entrypoint flow to accept a list of months, a year, and a taxi color.
Make any other necessary changes to the code for it to function as required.
Create a deployment for this flow to run in a local subprocess with local flow code storage (the defaults).
Make sure you have the parquet data files for Yellow taxi data for Feb. 2019 and March 2019 loaded in GCS. Run your deployment to append this data to your BiqQuery table. How many rows did your flow code process?

- 14,851,920
- 12,282,990
- 27,235,753
 - 11,338,483

ANSWER : 14851920
```
00:35:20.205 | INFO    | Flow run 'turquoise-lyrebird' - Current total rows 14851920
```

Question 4. Github Storage Block
```
01:42:39.854 | INFO    | Task run 'clean-2c6af9f6-0' - rows: 88605
```

Q5
```
01:49:31.145 | INFO    | Task run 'clean-2c6af9f6-0' - rows: 514392
```


Q6:  8
```
* * * * * * * *
```