class animal:
    pass
class pets(animal):
    pass
class dog(pets):
    @staticmethod
    def bark():
        print("MOOOOOOOOO!")

d=dog()

d.bark()