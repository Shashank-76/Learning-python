d={}#empty dictonary
marks={
    "shashank":100,
    "khusanoob":90,
    "animal":98,
    10:"shashank"
}
# print(marks.items())
# print(marks.keys())#left sidde ma bhako haru keys 
# print(marks.values())#rigth sidde ma bhako haru values
# marks.update({"shashank":99,"sanjay":89})
# print(marks.get("shashank"))
# print(marks["shashank"])


# print(marks.get("shashank2"))#prints none if get method is used
# print(marks["shashank2"])#returns an errror because square bracket is used

student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}


age = student.pop("age")

print(age)#Remove a key
print(student)

student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

student.popitem()#Remove last item
print(student)