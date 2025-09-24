# import sys
# sys.path.append("/workspaces/file_directory")

# from test2 import message -> file test2 in the directory, message function in test2

class Person:
    species = "Human"
print(Person.species)

man = Person()
print(man.species)

man.name = "Darth"
man.surname = "Vader"
print(man.name, man.surname)

class Dog:
    def bark(self):
        return "Woof! Woof!"
# create an object of dog
my_dog = Dog()
bark = my_dog.bark()
print(bark)

class Square:
    side = 9
    def area(self):
        return self.side ** 2
sq = Square()
sq.side = 24.8
print(sq.area())

# __init__ special method which is called when the object is created

class Cat:
    def __init__(self, name):
        self.name = name
kitty = Cat("Gypsy")
print(kitty.name)