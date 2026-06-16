# using walrus operator
if(n:=len([1,3,4,2,4]))>3:
    print(f"List is too long ({n} elements,expected <=3)")
    