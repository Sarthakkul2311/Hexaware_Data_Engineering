import pandas as pd 

filename='student_data.csv'
header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
data = pd.DataFrame(data, columns=header)
data.to_csv('student_data.csv', index=False)
print("data is inserted")