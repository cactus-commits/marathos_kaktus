# marathos_kaktus


initial setup 
- raw files in default folder 
- initial exploration of the data 

after initial exploration -> ingest in the bronz layer


%md
## Lessons

- `regexp_extract` can mask format anomalies when the regex is too broad — for example, 
  `"[a-zA-Z]+"` on `"250km/6Etappen"` returns `"km"`, hiding the full format complexity. 
  Running `distinct()` on the full column is safer for catching unexpected formats during data profiling.

### Pipeline design: historic vs streaming data

When combining static historic data with a streaming table in a single pipeline, 
Spark will reprocess the historic data on every pipeline run since it uses `spark.read` 
(not `spark.readStream`). For a school project this is acceptable, but in production 
the correct approach would be to split this into separate pipelines — one for historic 
data that runs once, and one for new incoming data that only processes new rows via 
`spark.readStream`. The union of the two sources would then happen in a third pipeline 
before the gold layer. This follows the DRY principle and avoids unnecessary reprocessing 
of data that never changes.