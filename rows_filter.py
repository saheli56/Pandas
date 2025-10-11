import pandas as pd
data ={
    'Name': ['Alice', 'Bob', 'Charlie','David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'salary': [50000, 60000, 70000, 80000, 90000],
}
df = pd.DataFrame(data)
# Filter rows where Age is greater than 30
#single condition
older= df[df['Age']>30]
print(older)
#multiple conditions
#age greater than 30 and salary greater than 70000
filtered = df[(df['Age']>30)& (df['salary']>70000)]
print('age greater than 30 and salary greater than 70000')
print(filtered)
#using or function
#age greater than 30 or salary greater than 70000
filtered_or = df[(df['Age']>30) | (df['salary']>70000)]
print('age greater than 30 or salary greater than 70000')
print(filtered_or)