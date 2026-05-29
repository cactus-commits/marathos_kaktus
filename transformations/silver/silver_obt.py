from pyspark import pipelines as pd
from utilities.utils import rename_columns_to_snackecase
from pyspark.sql.functions import col, to_timestamp,to_date, when, round as spark_round



# slå ihop till en table 
@dp.table(
    name="marathos.silver.marathos_obt",
    comment="Cleaned historic race data and new race data for Marathos",
    table_properties={
        "delta.columnMapping.mode": "name",
        "delta.minReaderVersion": "2",
        "delta.minWriterVersion": "5"
    },
)

def silver_obt():
    df_historic = spark.sql("FROM STREAM marathos.bronze.um_races_raw")
    df_new = spark.sql("FROM STREAM marathos.bronze.new_race_data")
    
    # Slå ihop till en tabell
    df = df_historic.union(df_new)

    # 1.Rename to snackecase
    df = rename_columns_to_snackecase(df)
    
    # 2. Drop rows and columns

    df = df.filter(
    col("event_distance_length").isNotNull() &     # nulls
    ~col("event_distance_length").rlike("d$") &    # unit is days(d)
    ~col("event_distance_length").rlike("x$") &    # unit is x
    ~col("event_distance_length").rlike("^[0-9:.]+$") # no unit in string
) 
    df = df.drop("event_distance_length")

    # 3. Change typos/standardize formats

    df = df.withColumn(
    "athlete_age_category",
    when(col("athlete_age_category") == "F35", "W35"). # fix typo
    otherwise
        (col("athlete_age_category"))
    
)
    df = df.withColumn("athlete_country", upper(col("athlete_country"))) # change to uppercase
    
    df = df.withColumn( # fix typos
    "athlete_country",
    when(col("athlete_country") == "SVE", "SWE")
    .when(col("athlete_country") == "GRB", "GBR")
    .when(col("athlete_country") == "IRE", "IRL")
    .when(col("athlete_country") == "XXX", "Unknown")
    .otherwise
        (col("athlete_age_category"))
)


    
    # Kör samma cleaning på båda
    return clean_races(df)