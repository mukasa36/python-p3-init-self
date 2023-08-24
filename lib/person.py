#!/usr/bin/env python3

class Person:
    def __init__(self, name="Guido"):
        self.name = name

# Create an instance of the Person class with the default name "Guido"
default_person = Person()
print(f"Default person's name is {default_person.name}")

# Create an instance of the Person class with a specific name
custom_person = Person("Alice")
print(f"Custom person's name is {custom_person.name}")
