# DENSE RANK, ORDER BY, ROUND, CAST, WHERE
# Import your libraries
import pyspark
from pyspark.sql import Window
from pyspark.sql.functions import col, round, dense_rank

# Start writing code
window1 = Window.orderBy(col("density").asc())
window2 = Window.orderBy(col("density").desc())

cities_density = cities_population.withColumn(
    "density", round(col("population") / col("area")).cast("int")
).dropna(subset=["density"])

ranked_cities = cities_density.withColumns({
    "ascending_rk": dense_rank().over(window1),
    "descending_rk": dense_rank().over(window2)
})

extreme_density_cities = ranked_cities.select(
    "country",
    "city",
    "density"
    ).where(
        (col("ascending_rk") == 1) |
        (col("descending_rk") == 1)
    )

# To validate your solution, convert your final pySpark df to a pandas df
extreme_density_cities.toPandas()