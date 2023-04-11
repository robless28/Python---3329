'''
Polymorphism 
Multiple classes with similar methods 
    - Not neesasary to be inherited 
'''

# Create a class cat, dog, cow 
    # each class should have a methd=od called speak()
        # but the implementation is different for each 

# __str__(self) method 


class Cat:
    def __init__(self):
        pass
    def speak(self):
        print("*Meow*")
        
    def __str__(self):
        self.speak()
        return "This is a cat"

class Dog:
    def speak(self):
        print("*Woof*")

class Cow:
    def speak(self):
        print("yes?")

# call the speak() method on 3 objects
aCow = Cow()
aCat = Cat()
aDog = Dog()

# make a list of animals 
animals = [aCat, aDog, aCow]

for animal in animals:
    animal.speak()

# polymorphism in python implementation 
print(7 + 2)
print("hello " + "class!")
print([6, 7, 8] + [1, 2, 3])
print(aCat)