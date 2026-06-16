# with finally
def fun():
    try:
        a=int(input("Enter a number: "))
        print(a)
        return

    except Exception as e:
         print(e)
         return

    finally:# runs regardless the error
        print("Thank You !!!")

fun()
 
#without Finally
def fun():
    try:
        a=int(input("Enter a number: "))
        print(a)
        return

    except Exception as e:
         print(e)
         return


    print("Thank You !!!")

fun()
 