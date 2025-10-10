import pandas as pd
data ={
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)
df.to_csv('people.csv', index=False)
df.to_excel('people.xlsx', index=False)
df.to_json('people.json', index=False)