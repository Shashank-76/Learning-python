import pandas as pd

df = pd.read_csv("chapter15_pandas.py/data.csv")
#selection by  column
print(df['Name'])
print(df['Height'])
print(df['Weight'])
print(df[['Name','Height','Weight']])

#selection by rows
print(df.loc[2])

#to print using a certain name
df = pd.read_csv("chapter15_pandas.py/data.csv",index_col="Name")
print(df.loc['Charmander'])
print(df.loc['Mewtwo',['Height','Weight']])
print(df.loc['Bulbasaur':'Charmeleon',['Height','Weight']])#print range
print(df.iloc[0:11:2,0:3])#0:3 select column

pokemon=input("Enter pokemon name:")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f'{pokemon} not found')