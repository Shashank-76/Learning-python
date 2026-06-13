class Employee:
    language="py"#THIS IS A CLASS ATTRIBUTE
    salary=120000

Khusanoob=Employee
Khusanoob.name="Khusanoob"#THIS IS A INSTANCE ATTRIBUTE
print(Khusanoob.name,Khusanoob.language,Khusanoob.salary)

Timber=Employee
Timber.name="Timber"
print(Timber.name,Timber.language,Timber.salary)

# HERE NAME IS INSTANCE ATTRIBUTE and SALARY AND LANGUAGE ARE CLASS AATTRIBUTE AS 
# THEY DIRECTLY BELONGS TO THE CLASS