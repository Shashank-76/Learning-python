try:
    a=int(input("Enter a number: "))
    print(a)

except Exception as e:
    print(e)
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
except TypeError as t:
    print(t)

print("Thank You !!!")
 