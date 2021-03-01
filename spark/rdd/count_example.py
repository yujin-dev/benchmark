from pyspark import SparkContext, SparkConf

""" word counting: parallelize -> count vs. countByValue """

if __name__ == "__main__":

    conf = SparkConf().setAppName("count").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    input_words = ["spark", "hadoop", "spark", "hive", "pig", "cassandra", "hadoop"]
    word_rdd = sc.parallelize(input_words)
    print(f"count :{word_rdd.count()}")
    
    word_count_value = word_rdd.countByValue()
    print(word_count_value)