name="ciggrate"

print(len(name))
print(name.endswith("ate"))
print(name.endswith("ates"))
print(name.startswith("cigg"))
print(name.startswith("wcigg"))
print(name.capitalize())
print(name.replace("ciggrate","icecream"))

text = "Python is awesome"

print(text.find("is"))      # 7
print(text.index("is"))     # 7
print(text.replace("awesome", "great"))

text = "HELLO WORLD"
print(text.lower())

text = "hello world"
print(text.upper())

text = "python programming"
print(text.title())

text = "   hello   "
print(text.strip())

text = "apple,banana,orange"
print(text.split(","))

fruits = ["apple", "banana", "orange"]
print(", ".join(fruits))

text = "Python Programming"
print(text.find("Program"))

text = "banana"
print(text.count("a"))

text = "12345"
print(text.isdigit())

text = "Python123"
print(text.isalnum())