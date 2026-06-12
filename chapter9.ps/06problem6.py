with open("text.txt") as f:
    content=f.read()
    
if ("python" in content):
    print("YES python is present...")
else:
    print("NO python is not present....")