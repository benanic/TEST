from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("SparkSessionTest") \
    .getOrCreate()

# Read a sample data file
data_path = "/Users/banic/Desktop/ExcelTest.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)

# Display the content of the DataFrame
df.show()

#change
