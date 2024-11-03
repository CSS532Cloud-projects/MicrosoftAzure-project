/*
Here are links to help you get started with Stream Analytics Query Language:
Common query patterns - https://go.microsoft.com/fwLink/?LinkID=619153
Query language - https://docs.microsoft.com/stream-analytics-query/query-language-elements-azure-stream-analytics */

-- Step 1: Save raw data
SELECT
    *
INTO
    iothw2container
FROM
    MyIotThingInputV2 

-- Step 2: Save Processed Data
SELECT
    System.Timestamp() AS EventTime,
    input.data AS rawData,
    UDF.calculateAverage(input.data) AS average_value
INTO
    "iothw2container-processed-data"
FROM
    MyIotThingInputV2 AS input