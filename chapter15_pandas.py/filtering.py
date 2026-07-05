import pandas as pd

df = pd.read_csv("chapter15_pandas.py/data.csv")
#filtering is keeping the rows that match the conditions

nd=df[df['Height']>=2]
wd=df[df['Weight']>100]
ld=df[df['Legendary']==1]# or true
md=df[df['Type1']=='Water']
gd=df[(df['Type1']=='Water') | (df['Type2']=='Water')]
print(nd)
print(wd)
print(ld,md,gd)
