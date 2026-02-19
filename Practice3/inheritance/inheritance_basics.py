# 1
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

d = Dog()
d.speak()


# 2
class Person:
    def walk(self):
        print("Walking")

class Student(Person):
    pass

s = Student()
s.walk()


# 3
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    pass

c = Car()
c.move()


# 4
class Bird:
    def fly(self):
        print("Flying")

class Eagle(Bird):
    pass

e = Eagle()
e.fly()
