#Map Example
l=[1,23,4,6,7,8]

square= lambda x:x*x

sqList =map(square,l)
print(list(sqList))

def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(squared)  # [1, 4, 9, 16, 25]

#Filter example

def even(n):
    if(n%2==0):
        return True
    return False
onlyeven=filter(even,l)
print(list(onlyeven))

#reduce Example
from functools import reduce
def sum(a,b):
    return a+b

mul= lambda x,y:x*y

print(reduce(sum,l))
print(reduce(mul,l))