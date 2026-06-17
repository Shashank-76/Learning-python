try:
    a=int(input('Enter you number a :'))
    b=int(input('Enter you number b :'))
    print(a/b)
except ZeroDivisionError as e:
    print("INFINITE")