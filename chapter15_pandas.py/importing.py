import pandas as pd

df = pd.read_csv("chapter15_pandas.py/data.csv")

# print(df)#prints the turncated version
print(df.to_string())


df = pd.read_json("chapter15_pandas.py/data1.json")
# print(df)#prints the turncated version
print(df.to_string())