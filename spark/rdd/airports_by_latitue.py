from pyspark import SparkContext, SparkConf
import pandas as pd
import time

""" 1. read data ( airports.text )
    2. find airports : latitude > 40
    columns: Airport ID, Name of airport, Main city served by airport, Country where airport is located, IATA/FAA code,
    ICAO Code, Latitude, Longitude, Altitude, Timezone, DST, Timezone in Olson format
"""


if __name__ == "__main__":


    with open("data/airports.text", "r") as f:
        data = f.readlines()
    test = data[:10]
    test = list(map(lambda x: x.split(","), test))
    test = list(filter(lambda x: float(x[6])>40, test))

    conf = SparkConf().setAppName("latitude").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    data = sc.textFile("data/airports.text")
    data = data.map(lambda x: x.split(","))
    data = data.filter(lambda x: float(x[6])>40)
    data = data.map(lambda x: f"{x[1]}: {x[6]}")
    print(data.take(20))