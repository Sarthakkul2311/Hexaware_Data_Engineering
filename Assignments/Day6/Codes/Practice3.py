import csv

filepath = "example2.csv"

# Open the file in read-and-write mode ('r+')
with open(filepath, 'r+', newline="") as file:
    csvwriter = csv.writer(file)
    
    # Move the file pointer to the end of the file to append data
    file.seek(0, 2)  # Seek to end of file
    
    # Data to append
    additional_data = [
        [6, "Liam", 23, 1],
        [7, "Emma", 22, 2]
    ]
    
    # Append the new data rows
    csvwriter.writerows(additional_data)

print("Data has been appended successfully.")
