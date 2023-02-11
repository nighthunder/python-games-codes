# INHERITANCE

class Animal():

    def __init__(self) -> None:
        print("Animal created")

    def who_am_i(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")

""" mye = Animal();
mye.who_am_i()
mye.eat() """

class Dog(Animal): # inheritance

    def __init__(self) -> None:
        Animal.__init__(self)
        print("DOG CREATED")

    def bark(self):
        print("AU AU")

mye = Dog();
mye.who_am_i()
mye.eat()
mye.bark()
    
# SPECIAL METHODS

class Book():
    def __init__(self, title, author, pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title {}, author {}, pages {}".format(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed!")

b = Book("Python's bible", "Jose PAdilha", 534)
print(len(b))
# del b # this is destroying the object: NameError: name 'b' is not defined
print(b)

