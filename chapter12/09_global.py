a=90#global variable
def fun():
    global a #makes the a in function a global variable
    a=3# local variable of function
    print(a)

fun()
print(a)