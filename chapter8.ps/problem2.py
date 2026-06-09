def f_to_c(f):
    c= 5*(f-32)/9
    return c

f=float(input("Enter temprature in fahrenieht :"))
b=f_to_c(f)
print(f"the temprature is {round(b,2)}")
