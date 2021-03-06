from pyspark.sql import SparkSession

"""
group by location
aggregate avg price per SQ Ft
sort by avg price per SQ Ft
    +----------------+-----------------+
    |        Location| avg(Price SQ Ft)|
    +----------------+-----------------+
    |          Oceano|             95.0|
    |         Bradley|            206.0|
    | San Luis Obispo|            359.0|
    |      Santa Ynez|            491.4|
    |         Cayucos|            887.0|
    |................|.................|
    |................|.................|
    |................|.................|
"""

if __name__ == "__main__":
    
    target_col = "Price SQ Ft"

    session = SparkSession.builder.appName("RealStateSQL").getOrCreate()
    df_reader = session.read

    response = df_reader.option("header", "true").option("inferSchema", value=True)\
        .csv("data/RealEstate.csv")

    response.printSchema()

    target_res = response.select("Location", target_col)
    target_res.show()
    target_res = target_res.groupBy("Location").avg(target_col)
    target_res.show()
    target_res.orderBy("avg(Price SQ FT)").show()


