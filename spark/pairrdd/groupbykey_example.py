from pyspark import SparkContext, SparkConf
import pandas as pd
import time

""" 1. read data ( airports.text )
    2. each country - list of airport names
    columns: Airport ID, Name of airport, Main city served by airport, Country where airport is located, IATA/FAA code,
    ICAO Code, Latitude, Longitude, Altitude, Timezone, DST, Timezone in Olson format
"""


if __name__ == "__main__":

    conf = SparkConf().setAppName("filter").setMaster("local[*]")
    sc = SparkContext(conf=conf)
    data = sc.textFile("data/airports.text")
    data = data.map(lambda x: x.split(","))

    pair_rdd = data.map(lambda x: (x[3], x[1]))
    grouped_rdd = pair_rdd.groupByKey()
    output = grouped_rdd.collectAsMap()
    print({key: list(value) for key, value in output.items()})