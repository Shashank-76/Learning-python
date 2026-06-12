with open("text.txt") as f:
    lines=f.readlines()
lineno=1
for line in lines: 
    if ("python" in line):
        print(f"YES python is present in line:{lineno}")
        break
    lineno+=1

else:
    print("NO python is not present....")   