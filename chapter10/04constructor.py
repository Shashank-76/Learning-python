class Employee:
    language="python"#THIS IS A CLASS ATTRIBUTE
    salary=120000

    def __init__(self,name,salary,language): #dunder method which is automatically called
        self.name= name
        self.salary=salary
        self.language=language 
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}\nThe salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning")

Timber=Employee("Timber",4000000,"C++")
print(Timber.name,Timber.salary,Timber.language)
