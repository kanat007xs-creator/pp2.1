# 1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

s = Student("Kanat", 17)
print(s.name, s.age)


# 2
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")

d = Dog()
d.speak()


# 3
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, year):
        super().__init__(brand)
        self.year = year

c = Car("Toyota", 2020)
print(c.brand, c.year)


# 4
class A:
    def hello(self):
        print("Hello from A")

class B(A):
    def hello(self):
        super().hello()
        print("Hello from B")

b = B()
b.hello()
