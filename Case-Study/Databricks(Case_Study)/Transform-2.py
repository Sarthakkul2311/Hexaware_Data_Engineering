# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("ETL_Students_Transform").getOrCreate()

# Read data
extracted_data_path = "dbfs:/user/hive/warehouse/students_extracted"
students_df = spark.read.format("delta").load(extracted_data_path)

# Transformation: filtering students above age 21
transformed_df = students_df.filter(col("Age") > 21)

transformed_data_path = "dbfs:/user/hive/warehouse/students_transformed"
transformed_df.write.format("delta") \
    .option("mergeSchema", "true") \
    .mode("overwrite") \
    .save(transformed_data_path)

transformed_df.show()

dbutils.notebook.exit("Transformation Completed")


# COMMAND ----------

