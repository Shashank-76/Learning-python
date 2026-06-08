marks1=int(input("Enter number 1:"))
marks2=int(input("Enter number 2:"))
marks3=int(input("Enter number 3:"))

#check for total percentage
total_percentage=float(100*(marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Congratulations! you have passed the exam\n Your marks are:",marks1,marks2,marks3,"\nYour percentage is:",total_percentage)
else:
    print("you failed try again next year\n Your marks are:",marks1,marks2,marks3,"\nYour percentage is:",total_percentage)