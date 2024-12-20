# Databricks notebook source
# File location and type
file_location = "/FileStore/tables/email.csv"
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

from pyspark.sql import SparkSession

spark = SparkSession.builder \
                    .appName('pyspark_ex').getOrCreate()

data = [('James','Smith','M',3000),
  ('Anna','Rose','F',4100),
  ('Robert','Williams','M',6200), 
]

columns = ["firstname","lastname","gender","salary"]
df = spark.createDataFrame(data=data, schema = columns)
df.show()

#1.write a program for adding a new column
from pyspark.sql.functions import lit
df.withColumn("new_column",lit(1)).show()
df.withColumn("other_column",df.salary*10).show()

# COMMAND ----------

#to create rdds and  dataframe
#
from pyspark import SparkContext
from pyspark.sql import  SparkSession

sc =SparkContext.getOrCreate()
spark = SparkSession.builder.appName('pyspark first program').getOrCreate()

data =spark.read.csv("/FileStore/tables/email.csv",header = True,inferSchema = True)

data.limit(10).toPandas
data.show()
display(data)

# COMMAND ----------

#Converting Pandasdf to spark df
from pyspark import SparkContext
from pyspark.sql import  SparkSession

sc =SparkContext.getOrCreate()
spark = SparkSession.builder.appName('pyspark first program').getOrCreate()
import pandas as pd    
data = [['Scott', 50], ['Jeff', 45], ['Thomas', 54],['Ann',34]] 
  
# Create the pandas DataFrame 
pandasDF = pd.DataFrame(data, columns = ['Name', 'Age']) 
  
# print dataframe. 
print(pandasDF)

sparkdf =spark.createDataFrame(pandasDF)
sparkdf.show()
sparkdf.printSchema()

# COMMAND ----------

from pyspark.sql.types import StructType,StructField, StringType, IntegerType
mySchema = StructType([ StructField("First Name", StringType(), True)\
                       ,StructField("Age", IntegerType(), True)])

sparkDF2 = spark.createDataFrame(pandasDF,schema=mySchema)
sparkDF2.printSchema()
sparkDF2.show()

# COMMAND ----------

spark.conf.set("spark.sql.execution.arrow.enabled","true")
spark.conf.set("spark.sql.execution.arrow.pyspark.fallback.enabled","true")

pandasDF2=sparkDF2.select("*").toPandas
print(pandasDF2)

# COMMAND ----------

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('pyspark_ex4').getOrCreate()

from pyspark.sql.functions import col,expr

data=[("2019-01-23",1),("2019-06-24",2),("2019-09-20",3)]
spark.createDataFrame(data).toDF("date","increment") \
    .select(col("date"),col("increment"), \
      expr("add_months(to_date(date,'yyyy-MM-dd'),cast(increment as int))").alias("inc_date")) \
    .show()

# COMMAND ----------


