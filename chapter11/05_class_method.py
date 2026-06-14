class employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The classs attribute is {cls.a}")

e=employee()
e.a=45

e.show()