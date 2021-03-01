from pyspark import SparkContext, SparkConf

""" word counting """

if __name__ == "__main__":

    conf = SparkConf().setAppName("word count").setMaster("local[3]") # core : 3
    sc = SparkContext(conf = conf)

    lines = sc.textFile("data/word_count.text")
    words = lines.flatMap(lambda line : line.split(" "))
    wordcounts = words.countByValue() # dictionary({word: number})

    for word, count in wordcounts.items():
        print(f"{word}:{count}")
 

