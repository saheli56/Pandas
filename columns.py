import pandas as pd
data ={
    'Name': ['Alice', 'Bob', 'Charlie','David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'salary': [50000, 60000, 70000, 80000, 90000]
}
df = pd.DataFrame(data)
df['Bonus'] = df['salary'] * 0.1
print(df)
# insert coloumn at specific location   
df.insert(0,'ID', [1,2,3,4,5])
print(df)