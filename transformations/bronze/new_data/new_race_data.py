from pyspark import pipelines as dp

BASE_DIR = "/Volumes/marathos/default/raw"

schema = spark.read.format("csv").options(header="true", inferSchema="true").load(f"{BASE_DIR}/new_data/new_race_data.csv").schema
                                                                             
@dp.table(
     name="marathos.bronze.new_race_data",
     comment="New race data from 2023 onwards - Bronze layer",
     table_properties={"delta.columnMapping.mode": "name"}
)                                                                       
def bronze_new_race_data_raw():
    return spark.readStream.format("csv").options(header="true").schema(schema).load(f"{BASE_DIR}/new_data")