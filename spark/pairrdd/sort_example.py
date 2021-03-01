from pyspark import SparkContext, SparkConf

""" 1. read data ( word_count.text )
    2. word counting : in descending order
""" 

if __name__ == "__main__":


    conf = SparkConf().setAppName("sorting").setMaster("local[1]")
    sc = SparkContext(conf = conf)

    sc = sc.textFile("data/word_count.text")
    data = sc.flatMap(lambda x: x.split(' '))

    count_pairrdd = data.map(lambda x: (x, 1))
    count_sum = count_pairrdd.reduceByKey(lambda x, y: x+y)

    sorted_count_sum = count_sum.sortBy(lambda x: x[1], ascending=False)
    print(sorted_count_sum.collect())