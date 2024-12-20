import csv

filepath = "example2.csv"

# Open the file in write mode ('w') which overwrites any existing data
with open(filepath, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    
    # Write header row
    csvwriter.writerow(["Id", "Name", "Age", "Courses_Enrolled"])
    
    # Data to write
    data = [
        [1, "Aparna", 20, 3],
        [2, "Stella", 20, 1],
        [3, "Kishore", 21, 4]
    ]
    
    # Write the data rows
    csvwriter.writerows(data)

print("Writing has been completed")