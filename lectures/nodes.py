""" mylist = [1,2,3]

mylist.append(4);
print(mylist);
print(type(mylist))
print(type(4))
print(type(20.0))
print(type("teste")) """ # shift + alt + A

class Sample():
    pass

x = Sample()
print(type(x))

class Dog():
    def __init__(self, breed) -> None:
        self.breed = breed

mydog = Dog(breed="Shitzu")
print(mydog.breed)