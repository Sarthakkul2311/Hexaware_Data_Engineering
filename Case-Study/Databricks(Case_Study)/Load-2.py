# Databricks notebook source
from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("ETL_Students_Load").getOrCreate()

# Read the transformed data 
transformed_data_path = "dbfs:/user/hive/warehouse/students_transformed"
transformed_df = spark.read.format("delta").load(transformed_data_path)

# Load: Save the transformed data (original Delta table location)
data_path = "dbfs:/user/hive/warehouse/students_copy"

transformed_df.write.format("delta") \
    .option("overwriteSchema", "true") \
    .mode("overwrite") \
    .save(data_path)

transformed_df.show()

dbutils.notebook.exit("Load Completed")


# COMMAND ----------

