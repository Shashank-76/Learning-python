class Employee:
    company="FCB"
    name="Random Name"
    def show(self):
        print(f"The name of the employee is {self.name} and the name of the company is {self.company}")


class language:
    language="Python"
    def print_language(self):
        print(f"The name of the employee is {self.name} and the languaage is {self.language}")

class programmer(Employee,language):
     language="Python"
     company="MNU"
     def show_language(self):
        print(f"The name of the employee is {self.name} and the languaage is {self.language}")

a=Employee()
b=programmer()
print(a.company,b.company)
b.show()
b.print_language()
b.show_language()