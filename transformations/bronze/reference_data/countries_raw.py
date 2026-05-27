from pyspark import pipelines as dp

BASE_DIR = "/Volumes/marathos/default/raw"

schema = spark.read.format("csv").options(header="true", inferSchema="true").load(f"{BASE_DIR}/reference_data/countries.csv").schema
                                                                             
@dp.table(
     name="marathos.bronze.countries_raw",
     comment="Country reference data - Bronze layer",
     table_properties={"delta.columnMapping.mode": "name"}
)                                                                       
def bronze_countries_raw():
    return spark.read.format("csv").options(header="true").schema(schema).load(f"{BASE_DIR}/reference_data/countries.csv")