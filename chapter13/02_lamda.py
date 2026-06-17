#without using lamda function
def square(n):
    return n * n

print(square(5))  # 25

#using lamda function
square = lambda n: n * n

print(square(5))  # 25