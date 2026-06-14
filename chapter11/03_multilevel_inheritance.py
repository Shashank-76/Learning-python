class employee:
    a=2
class programmer(employee):
    b=3
class manager(programmer):
    c=4

o= employee()
print(o.a)

o=programmer()
print(o.a,o.b)

o=manager()
print(o.a,o.b,o.c)