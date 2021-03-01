from pyspark import SparkContext, SparkConf

""" parallelize -> reduce  """

if __name__ == "__main__":

    conf = SparkConf().setAppName("reduce").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    input_integers = [1,2,3,4,5]
    int_rdd = sc.parallelize(input_integers)

    product = int_rdd.reduce(lambda x, y: x*y)
    print(product)
