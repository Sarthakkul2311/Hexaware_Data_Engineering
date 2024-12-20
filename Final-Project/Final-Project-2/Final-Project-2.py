# Databricks notebook source
storage_account_name = "sarthakstoragelake"
container_name = "sarthak-project-container-2"
storage_account_key = "XlDzU3KO3qWAPtob6Ub5HUaiRvY6YlWHAOFpV7jTXjTC314YGoDfBYCNkVSp2/H+HtHFy++rMOWm+ASt7d+vWQ=="

# Set the Spark configuration to access the Azure Data Lake Storage Gen2 account
spark.conf.set(
    f"fs.azure.account.key.{storage_account_name}.dfs.core.windows.net",
    storage_account_key
)

# Define the input path for Data Lake
input_path = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/"

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType, FloatType, IntegerType
from pyspark.sql.functions import col, to_date, date_format

# Define schema for your dataset
schema = StructType([
    StructField("User_ID", StringType(), True),        # Unique identifier for each user
    StructField("Product_ID", StringType(), True),     # Unique identifier for each product
    StructField("Category", StringType(), True),       # Product category
    StructField("Price (Rs.)", FloatType(), True),     # Original price of the product
    StructField("Discount (%)", IntegerType(), True),  # Discount applied to the product
    StructField("Final_Price(Rs.)", FloatType(), True),# Final price after discount
    StructField("Payment_Method", StringType(), True), # Payment method used
    StructField("Purchase_Date", StringType(), True)   # Date of purchase
])

# Define the path to your Azure Data Lake Storage Gen2
input_path = f"abfss://{container_name}@{storage_account_name}.dfs.core.windows.net/"

# Read the streaming data
streaming_df = spark.readStream \
    .format("csv") \
    .option("header", "true") \
    .schema(schema) \
    .load(input_path)

# Transformation 1: Add Total_Sales
transformed_df = streaming_df.withColumn("Total_Sales", 
                                         col("`Final_Price(Rs.)`") * (100 - col("`Discount (%)`")) / 100)

# Transformation 2: Filter data (e.g., filtering categories or price)
filtered_df = transformed_df.filter(col("`Category`").isNotNull())

# Transformation 3: Format the 'Purchase_Date' to 'yyyy-MM-dd' format
final_df = filtered_df.withColumn(
    "Formatted_Purchase_Date", 
    date_format(to_date(col("`Purchase_Date`"), "dd-MM-yyyy"), "yyyy-MM-dd")
)

# You can now display the final DataFrame
print(final_df.columns)

# COMMAND ----------

# Define the storage account name and key
storage_account_name_2 = "sarthakprojectlake2"
storage_account_key_2 = "CJnXdrz3Jj57eXHseLVQ+cMTfzuV1+7lHB1yrZYZ1CeHVg7pUdKfVbtKQteKyx/yHUFeZbuv3lRI+AStHXVwMg==" # Make sure this key is correct

# Set the Spark configuration for accessing Azure Data Lake
spark.conf.set(
    f"fs.azure.account.key.{storage_account_name_2}.dfs.core.windows.net",
    storage_account_key_2
)

# Specify the output and checkpoint path for Data Lake
output_container_name = "sarthak-container-2"
checkpoint_container_name = "checkpoint-2"
output_path = f"abfss://{output_container_name}@{storage_account_name_2}.dfs.core.windows.net/output/final_output_data.csv"
checkpoint_path = f"abfss://{checkpoint_container_name}@{storage_account_name_2}.dfs.core.windows.net/checkpoint/"

# Write the transformed data to the output path in CSV format
query = final_df.writeStream \
    .format("csv") \
    .option("path", output_path) \
    .option("checkpointLocation", checkpoint_path) \
    .option("header", "true") \
    .outputMode("append") \
    .start()

# Wait for the termination of the streaming job
query.awaitTermination()
