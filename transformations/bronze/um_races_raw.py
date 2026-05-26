from pyspark import pipelines as dp

BASE_DIR = "/Volumes/marathos/default/raw"

schema = spark.read.format("csv").options(header="true", inferSchema="true").load(f"{BASE_DIR}/TWO_CENTURIES_OF_UM_RACES.csv").schema
                                                                             
@dp.table(
     name="marathos.bronze.um_races_raw",
     comment="Raw data for Marathos - Bronze layer",
     table_properties={"delta.columnMapping.mode": "name"}
)                                                                       
def bronze_um_races_raw():
    return spark.readStream.format("csv").options(header="true",encoding="latin1").schema(schema).load(BASE_DIR)