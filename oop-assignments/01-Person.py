# Create a class Person and perform specified methods
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}.")

# Input:
person1 = Person("Sreshtha", 19, "female")
person1.introduce()                      
