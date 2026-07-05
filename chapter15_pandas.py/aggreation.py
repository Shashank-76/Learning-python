import pandas as pd

# aggregate function:Reduce a set of values into a single value. used to summarize and analyse data. often used by the groupby() function

df=pd.read_csv("chapter15_pandas.py/data.csv")


# print(df)

# #whole dataframe
# print(df.mean(numeric_only=True))#to find mean 
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count)

#single column
# print(df['Height'].mean())#to find mean 
# print(df['Height'].sum())
# print(df['Height'].min())
# print(df['Height'].min())
# print(df['Height'].max())
# print(df['Height'].count())

#groupby
group=df.groupby('Type1')

print(group['Height'].mean())
print(group['Height'].sum())
print(group['Height'].min())
print(group['Height'].max())
print(group['Height'].count())
