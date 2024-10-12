# DENSE RANK, ORDER BY, GROUP BY, SUM, WHERE, SELECT
# Import your libraries
import pyspark
from pyspark.sql import Window
from pyspark.sql.functions import col, dense_rank, desc, sum

window = Window.orderBy(col("profits").desc())

# Start writing code
result = forbes_global_2010_2014.groupBy("company") \
    .agg(sum("profits").alias("profits")) \
    .withColumn(
    "profit_rank", dense_rank().over(window)
    ).where(col("profit_rank") <= 3) \
    .select("company", "profits") \
    .orderBy(col("profits").desc())

# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()