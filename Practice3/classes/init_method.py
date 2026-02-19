# 1
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Kanat")
print(p.name)

# 2
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c = Car("Toyota", 2020)
print(c.brand, c.year)

# 3
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Kanat", 17)
print(s.name, s.age)

# 4
class Book:
    def __init__(self, title):
        self.title = title

b = Book("Python Basics")
print(b.title)
