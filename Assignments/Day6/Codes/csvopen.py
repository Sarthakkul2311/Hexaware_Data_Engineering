import csv
import os

# Define the path to the CSV file
file_path = "C:/Users/Sarthak Kulkarni/Desktop/Hexaware Python Training/Data_engineering/Python_codes/example2.csv"
# Check if the file exists before opening it
if os.path.exists(file_path):
    # Open the file in read mode
    with open(file_path, mode="r") as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            print(row)  # Print each row
else:
    print("The file does not exist.")


