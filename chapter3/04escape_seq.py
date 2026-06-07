a="smoking kills \nwe should not smoke \n you will die" 
print(a)
a="smoking kills \twe should not smoke \t you will die" 
print(a)
a="smoking kills \nwe should not smoke \" you will die\"" 
print(a)
print("C:\\Users\\Alice")#C:\Users\Alice
print("Hello\rHi")#"Hi" overwrites the first two characters of "Hello".
print("Helloo\b")#Removes the character before it.
path = r"C:\Users\Alice\Documents"
print(path)#To prevent Python from interpreting escape sequences:
#Without r, Python would try to interpret sequences like \n and \t.