import pandas as pd
import json

df = pd.read_csv("chapter15_pandas.py/data.csv")
json_data = df.to_json(orient="records", indent=2)

with open("chapter15_pandas.py/data1.json", "w") as f:
    f.write(json_data)

print("Saved as data1.json!")