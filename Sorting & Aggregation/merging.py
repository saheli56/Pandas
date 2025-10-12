import pandas as pd

#customer dataframe

df_1 = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David']
})

#order dataframe
df_2 = pd.DataFrame({
    'OrderID': [101, 102, 103, 104],
    'CustomerID': [1, 2, 1, 3],
    'Product': ['Widget', 'Gadget', 'Doodad', 'Thingamajig']
})
#merge dataframes on CustomerID
print(pd.merge(df_1, df_2, on = "CustomerID", how = "inner"))