from pyspark import SparkContext, SparkConf
import time

""" 1. read data ( prime_nums.text )
    2. sum 
"""

if __name__ == "__main__":

    # list
    st = time.time()
    with open("data/prime_nums.text", "r") as f:
        data = f.readlines()
    data = list(map(lambda x: x.split("\t"), data))
    data = sum(data, [])
    data = list(map(lambda x: int(x.strip()), data))
    sum_rdd = sum(data)
    print(f"list SUM: {sum_rdd}")
    print(time.time() - st)

    # spark 
    st = time.time()
    conf = SparkConf().setAppName("sum").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    rdd = sc.textFile("data/prime_nums.text")
    rdd = rdd.flatMap(lambda x: x.split("\t"))
    rdd = rdd.map(lambda x: int(x.strip())) # rdd.collect() 로 확인
    sum_rdd = rdd.reduce(lambda x, y: x+y)
    print(f"spark SUM: {sum_rdd}")
    print(time.time() - st)
