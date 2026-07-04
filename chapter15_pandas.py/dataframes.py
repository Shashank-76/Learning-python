import pandas as pd

data={"name":['Spongebob','Patrick','Squidward'],
      'age':[15,11,29]}

df=pd.DataFrame(data,index= ["Employee#1",'Employee#2','Employee#3'])
#add a new column
df["job"]=["cook","N/A",'cashier']
#add a new row
new_row=pd.DataFrame([{"name":'Sandy',"age":18,'job':'Engineer'},{'name':'Mr.crab','age':39,"job":'Manager'}],index=['Employee#4','Employee#5'])
df=pd.concat([df,new_row])
print(df)