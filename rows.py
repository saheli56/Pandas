#head(n) if n value is not given then it will return first 5 rows
#tail(n) if n value is not given then it will return last 5 rows
import pandas as pd
df = pd.read_csv('Salary_Data.csv')
print('Display first 10 rows of the dataframe')
print(df.head(10))
print('Display last 10 rows of the dataframe')
print(df.tail(10))