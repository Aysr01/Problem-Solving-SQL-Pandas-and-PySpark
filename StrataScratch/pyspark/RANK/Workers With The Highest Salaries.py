# ORDER BY, WHERE, INNER JOIN, DISTINCT, RANK
# Import your libraries
import pyspark
from pyspark.sql import Window
from pyspark.sql.functions import avg, col, rank

# Start writing code
window = Window.orderBy(col("salary").desc())
               
highest_paid_titles = worker.withColumn("rk", rank().over(window)) \
    .where(col("rk") == 1) \
    .join(title, worker.worker_id == title.worker_ref_id, "inner") \
    .select(
        col("worker_title").alias("best_paid_title")
        ) \
    .distinct()
# To validate your solution, convert your final pySpark df to a pandas df
highest_paid_titles.toPandas()