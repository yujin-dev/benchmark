from pyspark import SparkContext, SparkConf

""" 1. read data (airports.text )
    2. generate pair RDD( airport name : country name ) 
""" 

if __name__ == "__main__":

    conf = SparkConf().setAppName("latitude").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    data = sc.textFile("data/airports.text")
    data = data.map(lambda x: x.split(","))

    data = data.map(lambda x: (x[1], x[3])) # (key, value)
    data = data.mapValues(lambda x: x.upper()) # value에만 적용됨
    print(data.take(10))