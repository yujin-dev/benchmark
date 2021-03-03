from pyspark import SparkContext, SparkConf

""" 1. read data ( RealEstate.csv )
    2. average price ( different number of bedrooms )
""" 

class AvgCount:
    def __init__(self, price, count):
        self.price = price
        self.count = count


if __name__ == "__main__":


    conf = SparkConf().setAppName("house_avgprice").setMaster("local[3]")
    sc = SparkContext(conf = conf)

    lines = sc.textFile("data/RealEstate.csv")
    data = lines.map(lambda x: x.split(","))
    data = data.filter(lambda x: x[3] != "Bedrooms")
    data = data.map(lambda x: (x[3], AvgCount(float(x[2]), 1)))
    sum_data = data.reduceByKey(lambda x, y: AvgCount(x.price+y.price, x.count+y.count))
    avg_price = sum_data.mapValues(lambda x: x.price/x.count)
    
    print(avg_price.collect())