import pandas as pd

data_1= pd.DataFrame({
    "ID": [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})
data_2= pd.DataFrame({
    "ID": [1, 2, 4],
    'Name': ['Ayon', 'Becky', 'Dennis']
})
#concatenate dataframes
print(pd.concat([data_1, data_2],ignore_index=True))