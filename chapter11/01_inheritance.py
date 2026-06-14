class Employee:
    company="FCB"
    name="Random Name"
    def show(self):
        print(f"The name of the employee is {self.name} and the name of the company is {self.company}")


# class programmer:
#     company="MNU"
#     language="Python"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the name of the company is {self.company}")
#     def show_language(self):
#         print(f"The name of the employee is {self.name} and the languaage is {self.language}")

class programmer(Employee):
     language="Python"
     def show_language(self):
        print(f"The name of the employee is {self.name} and the languaage is {self.language}")

a=Employee()
b=programmer()
print(a.company,b.company)