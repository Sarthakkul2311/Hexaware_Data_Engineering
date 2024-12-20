# Databricks notebook source
#initialize the program
from pyspark import SparkContext
from pyspark.sql import  SparkSession

sc =SparkContext.getOrCreate()
spark = SparkSession.builder.appName('pyspark first program').getOrCreate()

#create the rdd

rdd = sc.parallelize([('C',85,76,87,91), ('B',85,76,87,91), ("A", 85,78,96,92), ("A", 92,76,89,96)])
print(type(rdd))


# COMMAND ----------


#to create rdds and  dataframe

# from pyspark import SparkContext
# from pyspark.sql import  SparkSession

# sc =SparkContext.getOrCreate()
# spark = SparkSession.builder.appName('pyspark first program').getOrCreate()

#create the rdd

rdd = sc.parallelize([('C',85,76,87,91), ('B',85,76,87,91), ("A", 85,78,96,92), ("A", 92,76,89,96)], 4)
sub = ['Division','English','Mathematics','Physics','Chemistry']
marks_df = spark.createDataFrame(rdd, schema=sub)
print(type(marks_df))
print(rdd)
marks_df.show()
marks_df.printSchema()

# COMMAND ----------

data =spark.read.csv("/FileStore/tables/email.csv")
data.show()
display(data)
data.show(10)

# COMMAND ----------

# File location and type
file_location = "/FileStore/tables/orders.csv"
file_type = "csv"

# CSV options
infer_schema = "false"
first_row_is_header = "false"
delimiter = ","

# The applied options are for CSV files. For other file types, these will be ignored.
df = spark.read.format(file_type) \
  .option("inferSchema", infer_schema) \
  .option("header", first_row_is_header) \
  .option("sep", delimiter) \
  .load(file_location)

display(df)

# COMMAND ----------

#to create rdds and  dataframe
#
from pyspark import SparkContext
from pyspark.sql import  SparkSession

sc =SparkContext.getOrCreate()
spark = SparkSession.builder.appName('pyspark first program').getOrCreate()

data =spark.read.csv("/FileStore/tables/email.csv",header = True,inferSchema = True)
data.show()
display(data)


# COMMAND ----------


 

# COMMAND ----------


