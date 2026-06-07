d={}
name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter language name: ")
d.update({name:lang})

print(d)

#if we want to print the language of a particular friend, we can use the key to access the value in the dictionary.
#  For example, if we want to print the language of "shashank", we can use the following code:

print(d["shashank"])

#if name of two friends is same then the value of the key will be updated to the latest value. 
# For example, if we enter the name "shashank" again and update the language to "java",
#  then the value of the key "shashank" will be updated to "java".
print(d)

#if the language of two friends with different names is same then both the keys will have the same value. 
# For example, if we enter the name "khusanoob" and update the language to "java",
#  then both the keys "shashank" and "khusanoob" will have the same value "java". because in dictionary the keys
#  are unique but the values can be same.