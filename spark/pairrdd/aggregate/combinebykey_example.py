from pyspark import SparkContext, SparkConf

""" combineByKey"""

if __name__ == "__main__":
    conf = SparkConf().setAppName("AverageHousePrice").setMaster("local")
    sc = SparkContext(conf = conf)

    lines = sc.textFile("data/RealEstate.csv")

    cleanedLines = lines.filter(lambda line: "Bedrooms" not in line)
    pair_rdd = cleanedLines.map(lambda x: (x.split(",")[3], float(x.split(",")[2])))

    create_combiner = lambda x: (1, x)
    merge_value = lambda avg, x: (avg[0]+1, avg[1]+x)
    merge_combiner = lambda a, b: (a[0]+b[0], a[1]+b[1])

    house_price = pair_rdd.combineByKey(create_combiner, merge_value, merge_combiner)
    
    house_avg = house_price.mapValues(lambda x: x[1]/x[0])
    print(house_avg.collect())

