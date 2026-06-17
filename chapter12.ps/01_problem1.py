# try:
#     with open("1.txt",'r') as f1, open("2.txt",'r') as f2 , open("3.txt",'r')as f3:
#         print(f1.read())
#         print(f2.read())
#         print(f3.read())
# except Exception as e:
#     print(e)
# print("Thank youu!!!")

files = ["1.txt", "2.txt", "3.txt"]

for file in files:
    try:
        with open(file, 'r') as f:
            print(f.read())
    except Exception as e:
        print(f"{file} is missing!")

print("Thank you!!!")