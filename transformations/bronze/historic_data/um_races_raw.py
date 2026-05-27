from pyspark import pipelines as dp

BASE_DIR = "/Volumes/marathos/default/raw"

schema = spark.read.format("csv").options(header="true", inferSchema="true").load(f"{BASE_DIR}/historic_data/TWO_CENTURIES_OF_UM_RACES.csv").schema
                                                                             
@dp.table(
     name="marathos.bronze.um_races_raw",
     comment="Histotic data for ultra marathons from 1789 - 2022 - Bronze layer",
     table_properties={"delta.columnMapping.mode": "name"}
)                                                                       
def bronze_historic_races_raw():
    return spark.read.format("csv").options(header="true",encoding="latin1").schema(schema).load(f"{BASE_DIR}/historic_data/TWO_CENTURIES_OF_UM_RACES.csv")