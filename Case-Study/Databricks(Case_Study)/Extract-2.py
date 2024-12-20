# Databricks notebook source
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("ETL_Students_Extract").getOrCreate()

# data path
data_path = "dbfs:/user/hive/warehouse/students_copy"

# Extract data 
students_df = spark.read.format("delta").load(data_path)

extracted_data_path = "dbfs:/user/hive/warehouse/students_extracted"
students_df.write.format("delta").mode("overwrite").save(extracted_data_path)

students_df.show()

dbutils.notebook.exit("Extraction Completed")


# COMMAND ----------

