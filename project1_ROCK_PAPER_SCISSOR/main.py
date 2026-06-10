import random
# '''
# rock wins over scissor
# scissor  wins over paper
# paper  wins over rock
# '''
computer=random.choice([1,-1,0])
choice=input("Enter your choice (r/p/s):")
dict1={"r":1,"p":-1,"s":0}
dict2={1:"Rock",-1:"Paper",0:"Scissor"}

if choice not in dict1:
    print("Invalid choice!")
    exit()

you=dict1[choice]

print(f"YOU CHOOSE {dict2[you]}\nCOMPUTER CHOOSE {dict2[computer]}")

if( computer==you):
    print("IT'S A DRAW")

else:
#     if(computer==1 and you==0 ): 
#         print("YOU LOSE")

#     elif(computer==0 and you==-1): 
#          print("YOU LOSE")

#     elif(computer==-1 and you==1): 
#          print("YOU LOSE")

#     elif(computer==0 and you==1 ): 
#          print("YOU WIN")

#     elif(computer==-1 and you==0): 
#          print("YOU WIN")

#     elif(computer==1 and you==-1 ):
#          print("YOU WIN")
#     else:
#         print("SOMETHING IS WRONG")
# the below logic is written on the basis of upper logic

    if((computer-you==1) or (computer-you==2)):
        print("YOU LOSE")
    else:
        print("YOU WIN")

     