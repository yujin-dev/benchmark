from pyspark import SparkContext, SparkConf

""" parallelize -> take  """

if __name__ == "__main__":

    conf = SparkConf().setAppName("take").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    word_rdd = sc.parallelize(input_words)

    words = word_rdd.take(3) # like pandas dataframe.head()
    print(words) # list