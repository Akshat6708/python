
class Animal:
    pass

class pets(Animal):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("bow bow !")

d= dog()
d.bark()