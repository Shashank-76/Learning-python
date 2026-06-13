class Employee:
    language="python"#THIS IS A CLASS ATTRIBUTE
    salary=120000

    def getInfo(self):
        print(f"The language is {self.language}\nThe salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning")

Khusanoob=Employee
Khusanoob.language="JavaScript"#THIS IS A INSTANCE ATTRIBUTE

Employee.greet()
Employee.getInfo(Khusanoob)
# Khusanoob.getInfo()
