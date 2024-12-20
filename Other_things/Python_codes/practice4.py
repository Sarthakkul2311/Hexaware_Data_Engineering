import csv

filepath = 'Myfiles.csv'

with open(filepath, 'w+', newline="") as file:
    csvwriter = csv.writer(file)
    
    csvwriter.writerow(["Id", "Name", "Age", "Courses_Enrolled"])
    
    data = [
        [10, "nikarna", 20, 3],
        [11, "nikella", 20, 1],
        [12, "nikshore", 21, 4]
    ]
    
    csvwriter.writerows(data)

print("Writing has been completed")