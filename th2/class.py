class MyClass:
    x=5
    
#a= MyClass()
#print(a.x)

class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def printname(self):
        print("My name is "+self.name)
#t=Student("Tran Minh Tam",22)
#print(t.name)
#print(t.age)
#t.printname()

# example for inheritance in python
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printname(self):
        print("My name is "+self.name)

class SV(Person):
    def __init__(self,name,age,mssv):
        Person.__init__(self,name,age)#or you can use super() like this     super().__init__(name,age) 
        self.mssv=mssv
    def printmssv(self):
        print(f"MSSV: {self.mssv}")
sv=SV("Tran Tam",22,1234567)
sv.printname()
sv.printmssv()