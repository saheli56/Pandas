import pandas as pd
data ={
    "Time": [1, 2, 3, 4, 5, 6],
    "Value": [10, None, None, 40, 50, 60]
}
df = pd.DataFrame(data)
print("Before Interpolation")
print(df)

df['Value'] = df['Value'].interpolate(method="linear")
print("After Interpolation")
print(df)
'''
timer series data
numberical data with trend
avoid dropping rows
'''