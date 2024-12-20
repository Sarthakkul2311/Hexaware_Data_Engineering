import csv
filepath='C:\\Users\\Aparna\\Desktop\\Hexaware Python\\CSVDemo\\Salary_Data.csv'
with open(filepath,'r') as csvfile:
    reader=csv.DictReader(csvfile)
    for row in reader:
        print(row)
    