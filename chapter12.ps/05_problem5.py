n=int(input("Enter your number:"))

table=[n*i for i in range(1,11)]
with open("chapter12.ps/tables.txt","a")as f:
    f.write(f"The table of {n} :{str(table)}\n")