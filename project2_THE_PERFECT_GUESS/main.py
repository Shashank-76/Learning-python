import random
n=random.randint(1,100)
a=-1
guesses=1
while(a!=n):
    a=int(input("Enter Your Guess:"))
    if(a<n):
        print("Higer Number Please!!")
        guesses+=1
    elif(a>n):
        print("Lower Number Please!!")
        guesses+=1
    
print(f"YAAYYYYYY!!! You have correctly guessed the number {n} in {guesses} guesses")