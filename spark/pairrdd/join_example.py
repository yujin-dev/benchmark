from pyspark import SparkContext, SparkConf

""" parallelize -> join
    이름 기준으로 join( name, age, address )
""" 

if __name__ == "__main__":
    
    conf = SparkConf().setAppName("JoinOperations").setMaster("local[1]")
    sc = SparkContext(conf = conf)

    ages = sc.parallelize([("Tom", 29), ("John", 22)]) 
    addresses = sc.parallelize([("James", "USA"), ("John", "UK")])

    join = ages.join(addresses)
    join.saveAsTextFile("result/age_address_join.text")
    
    left_outer_join = ages.leftOuterJoin(addresses)
    left_outer_join.saveAsTextFile("result/left_outer_join.text")

    right_outer_join = ages.rightOuterJoin(addresses)
    right_outer_join.saveAsTextFile("result/right_outer_join.text")

    full_outer_join = ages.fullOuterJoin(addresses)
    full_outer_join.saveAsTextFile("result/full_outer_join.text")
