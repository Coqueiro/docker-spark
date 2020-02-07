from pyspark.sql import SparkSession


def main():
    df = spark.read.json('s3a://lucas-spark-read-test/')
    df.show()

if __name__ == "__main__":
    spark = SparkSession.builder.appName('session_calc').getOrCreate()
    main()