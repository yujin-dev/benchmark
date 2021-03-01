from pyspark import SparkContext, SparkConf

""" word counting by pair RDD """

if __name__ == "__main__":
    conf = SparkConf().setAppName("wordCounts").setMaster("local[3]")
    sc = SparkContext(conf = conf)

    lines = sc.textFile("data/word_count.text")
    word_rdd = lines.flatMap(lambda x: x.split(" "))
    word_pair_rdd = word_rdd.map(lambda x: (x, 1))
    word_count = word_pair_rdd.reduce(lambda x, y: x+y)

    print(word_pair_rdd.collect())