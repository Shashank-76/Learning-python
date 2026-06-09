def good_day(name, ending):
    print("Good Day "+ name)
    print(ending)
good_day("shashank","THANK YOU!!!")


def avg():
    a=int(input("ENTER YOUR NUMBER:"))
    b=int(input("ENTER YOUR NUMBER:"))
    c=int(input("ENTER YOUR NUMBER:"))
    average=(a+b+c)/3
    return(average)

for  i in range(1,3):
    print(f"THE AVERAGE IS {avg()}")# avg() is the funtion call
    print("THANK YOU!!!")