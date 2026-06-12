f=open("poem.txt")
content=f.read()
if("timber" in content):
    print("The word timber is present in the content")
else:
    print("The word timber is not present in the content")

f.close()