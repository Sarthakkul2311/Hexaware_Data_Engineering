import csv

new_data = [
    ["Harinya", 32, "Andhra Pradesh"],
    ["Vikas", 21, "Kurnool"]
]

# File path to the CSV file
file_path = "C:/Users/Sarthak Kulkarni/Desktop/Hexaware Python Training/Data_engineering/Day6/example.csv"

# Open the file in append mode and write the new rows
with open(file_path, mode="a", newline="") as file:
    writer = csv.writer(file)
    
    # Write each row in new_data
    for row in new_data:
        writer.writerow(row)

print("Data appended successfully.")