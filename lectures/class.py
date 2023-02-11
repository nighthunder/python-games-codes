class Sample():
    pass

x = Sample()
print(type(x))

class Dog():

    # CLASS OBJECT ATTRIBUTE
    species = "cannis"

    def __init__(self, breed, name) -> None:
        self.breed = breed
        self.name = name

mydog = Dog(breed="Shitzu", name="Snowball")
otherdog = Dog("Husky", "Wolf")
""" print(mydog.breed)
print(otherdog.breed)
print(mydog.species) """

class Circle():

    pi = 3.14

    def __init__(self, radius=1) -> None:
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * self.pi

    def set_radius(self, radius):
        self.radius = radius

mycircle = Circle(radius=3)
mycircle.set_radius(4)
print(mycircle.radius)
print(mycircle.area())

