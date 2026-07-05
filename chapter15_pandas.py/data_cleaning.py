import pandas as pd

#data cleaning the process of fixing/removing:incorrect ,incomplete or irrelevant data.~75% of work done by panda is data cleaning

df=pd.read_csv("chapter15_pandas.py/data.csv")

#drop irrelevant columns
df=df.drop(columns=['Legendary','No'])

#handel missing data
df=df.dropna(subset=['Type2']) #removed rows with no type 2 values
df=df.fillna({'Type2':'None'})

#fix inconsistent values
df['Type1']=df['Type1'].replace({'Grass':'GRASS',
                                 'Fire':'FIRE'})

#Standardize text
df["Name"]=df["Name"].str.lower()

#fix/change data types
df['Legendary']=df['Legendary'].astype(bool)

#remove duplicate values
df=df.drop_duplicates()

print(df.to_string())