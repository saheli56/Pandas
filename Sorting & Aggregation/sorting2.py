import pandas as pd
data ={
    'Name': ['Alice', 'Bob', 'Charlie','David', 'Eva'],
    'Age': [None, 30, 35, 40, 45],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
df = pd.DataFrame(data)
df.sort_values(by=['Age', 'City'], ascending=[True,False], inplace=True)
print(df)