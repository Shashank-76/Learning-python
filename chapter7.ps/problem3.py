#using for loop
n=int(input("Enter any number"))

for i in range(2,n):
    if(n%i==0):
        print("The given number is not a prime number")
        break
else:
         print("The given number is a prime number")

# using while loop
n=int(input("Enter any  number:"))

i=2
while(i<n//2):
    if(n%i==0):
        print("The given number is not a prime number")
        break
    i+=1
else:
    print("The ggiven number is a prime number")
    