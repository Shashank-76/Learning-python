class demo:
    a=4

o=demo()
print(o.a)#prints the class attribute because the instance attribute is not present
o.a=0#instance attribute is created
print(o.a)#prints the instance attribute because the instance attribute is present
print(demo.a)#prints the class attribute