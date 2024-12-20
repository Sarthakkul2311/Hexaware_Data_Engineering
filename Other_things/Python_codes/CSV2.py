import pandas as pd
filename='c:\\Users\\Aparna\\Desktop\\Hexaware Python\\CSVDemo\\finance_csvfile.csv'
data=pd.read_csv(filename,encoding='ISO-8859-1')
data.columns
print(data.columns)
print(data.value)
