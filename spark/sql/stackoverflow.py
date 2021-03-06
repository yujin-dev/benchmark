from pyspark.sql import SparkSession

AGE_MIDPOINT = "age_midpoint"
SALARY_MIDPOINT = "salary_midpoint"
SALARY_MIDPOINT_BUCKET = "salary_midpoint_bucket"

if __name__ == "__main__":

    session = SparkSession.builder.appName("StackOverFlowSurvey").getOrCreate()
    df_reader = session.read

    response = df_reader\
    .option("header", "true")\
    .option("inferSchema", value=True)\
    .csv("data/2016-stack-overflow-survey-responses.csv")

    print("Schema")
    response.printSchema()

    print("Selected columns")
    res_selected_columns = response.select("country", "occupation", AGE_MIDPOINT, SALARY_MIDPOINT)
    res_selected_columns.show()

    print("Country = Afghanistan")
    res_selected_columns.filter(res_selected_columns["country"]=="Afghanistan").show()

    print("Count of occupations")
    res_selected_columns.groupby("occupation").count().show()

    print("Average mid age < 20")
    res_selected_columns.filter(res_selected_columns[AGE_MIDPOINT]<20).show()

    print("Sort salary middle point")
    res_selected_columns.orderBy(res_selected_columns[SALARY_MIDPOINT], ascending=False).show()

    print("Group by country -> aggregate by average middle point ")
    res_selected_columns.groupBy("country").avg(SALARY_MIDPOINT).show()

    print("Salary bucket columns")
    res_selected_bucket = response.withColumn(SALARY_MIDPOINT_BUCKET, ((response[SALARY_MIDPOINT]).cast("integer")))
    res_selected_bucket.select(SALARY_MIDPOINT, SALARY_MIDPOINT_BUCKET).show()

    print("Group by salary bucket")
    res_selected_bucket\
        .groupBy(SALARY_MIDPOINT_BUCKET)\
        .count()\
        .orderBy(SALARY_MIDPOINT_BUCKET)\
        .show()

    session.stop()