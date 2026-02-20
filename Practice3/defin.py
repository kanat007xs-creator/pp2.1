class Person():
    def __init__(self,name,age):
      self.name=name
      self.age=age
    def fg(self):
      print(f"my name is",self.name,"i am",self.age,"old")

a=Person("Kanat","18")
a.fg()

class Students(Person):
    def __init__(self,name,age,grade):
      super().__init__(name,age)
      self.grade=grade
    def fh(self):
       print(f"my name is",self.name,"i am",self.age,"old","my grade",self.grade)
a=Students("Kanat","18","4.00")
a.fh()

class Doctor(Person):
    def __init__(self,name,age,hos,pr):
      super().__init__(name,age)
      self.hos=hos
      self.pr=pr
    def fh(self):
      print("my name",self.name,"my age",self.age,"my hos",self.hos,"my pr",self.pr)

a=Doctor("Kanat","18","7 bal","aiti")
a.fh()