# 1
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

d = Dog()
d.speak()


# 2
class Person:
    def introduce(self):
        print("I am a person")

class Student(Person):
    def introduce(self):
        print("I am a student")

s = Student()
s.introduce()


# 3
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Bike(Vehicle):
    def move(self):
        print("Bike is moving")

b = Bike()
b.move()


# 4
class Bird:
    def fly(self):
        print("Bird is flying")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

p = Penguin()
p.fly()
