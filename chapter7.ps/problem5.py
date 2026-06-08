n=int(input("Enter the number:"))
i=1
fact=1
while(i<=n):
    fact=fact *i
    i +=1
    
print(f"The fact of {n} is :{fact}")

#for loop
n=int(input("Enter the number:"))
i=1
fact=1
for i in range(i,n+1):
    fact=fact *i
    
print(f"The fact of {n} is :{fact}")

