import random
def game():
    print("You are playing a game...")
    score= random.randint(1,62)
    # fetch the highscore
    with open("Hiscore.txt") as f:
        Hiscore= f.read()
        if(Hiscore!=""):
            Hiscore=int(Hiscore)
        else:
            Hiscore=0
    
    print(f"Your score is{score}")

    if(score>Hiscore):
        #write the hiscroe in the file
        with open("Hiscore.txt","w") as f:
            f.write(str(score))
    return(score)

game()        