import pandas as pd

# series=A pandas 1-D labeled array that  can hold any data type.Think of it a single column in spreadsheet (1-dimensional)
data=[100,101,102,"name",True]

series=pd.Series(data,index=["Apartment #1","Apartment #2","Apartment #3","name","false"])
# Series is a constructor not a function and index function gives custom indexing default is 0,1,2
print(series.loc['Apartment #1'])# loc used to locate specific value
series.loc["name"]="Khusanoob"# modify
series.iloc[3]#integer lock uses default indexing 0,1,2,3
print(series)

#filtering by values
data=[100,101,102,200,243]
series=pd.Series(data,index=["a","b","c","d","e"])
print(series[series<=199])

