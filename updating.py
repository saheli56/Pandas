import pandas as pd
data ={
    'Name': ['Alice', 'Bob', 'Charlie','David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'salary': [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)
df.loc[0,'Age']=26
print(df)
df['salary'] = df['salary'] + 5000
print(df)