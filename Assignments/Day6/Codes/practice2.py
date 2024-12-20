import csv

filepath = 'example2.csv'

# Open the file in write mode ('w'), which overwrites any existing data
with open(filepath, 'w', newline="") as file:
    csvwriter = csv.writer(file)  # Create a writer object
    
    # Write header row
    csvwriter.writerow(["Id", "Name", "Age", "Courses_Enrolled"])
    
    # Data to write
    data = [
        [6, "arna", 20, 3],
        [5, "ella", 20, 1],
        [4, "shore", 21, 4]
    ]
    
    # Write the data rows
    csvwriter.writerows(data)

print("Writing has been completed")
