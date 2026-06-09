def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * fact(n-1)
    
n=int(input("Enter your Number:"))
print(f"The factorial of given number {n} is {fact(n)}")
            