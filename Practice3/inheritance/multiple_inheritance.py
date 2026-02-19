# 1
class A:
    def hello(self):
        print("Hello from A")

class B:
    def hi(self):
        print("Hi from B")

class C(A, B):
    pass

c = C()
c.hello()
c.hi()


# 2
class Father:
    def work(self):
        print("Father works")

class Mother:
    def cook(self):
        print("Mother cooks")

class Child(Father, Mother):
    pass

child = Child()
child.work()
child.cook()


# 3
class Writer:
    def write(self):
        print("Writing")

class Speaker:
    def speak(self):
        print("Speaking")

class Person(Writer, Speaker):
    pass

p = Person()
p.write()
p.speak()


# 4
class Flyable:
    def fly(self):
        print("Flying")

class Swimmable:
    def swim(self):
        print("Swimming")

class Duck(Flyable, Swimmable):
    pass

d = Duck()
d.fly()
d.swim()
