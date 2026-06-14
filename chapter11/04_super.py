class employee:
    def __init__(self):
        print("Constructor of employee")
    a=2
class programmer(employee):
    def __init__(self):
        super().__init__()
        print("Constructor of programmer")
    b=3
class manager(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of manager")
    c=4

o= employee()
print(o.a)

o=programmer()
print(o.a,o.b)

o=manager()
print(o.a,o.b,o.c)