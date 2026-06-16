dict1 ={"a":2,"b":23}
dict2 ={"b":4,"c":43}
merged = dict1|dict2
print(merged)

with open("file1.txt") as f1, open("file2.txt") as f2:
    print(f1.read())
    print(f2.read())
