'''class bird:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fly(self):
        print("fly fly")
class ket(bird):
    def __init__(self,eat):
        super().__init__()
        self.eat=eat
    def run(self):
        print("run run")'''


'''class bird:
    def __input__(self):
        a=input("nhap 1")
        b=input("nhap 2")
    def fly(self):
        print("fly fly")
class ket(bird):#inheritance
    def __input__(self):
        super().__input__()
        c=input("nhap 3")
    def run(self):
        print("run run")
a=ket()
a.__input__()'''


class bird:
    def __input__(self):
        a=input("nhap 1")
        b=input("nhap 2")
    def fly(self):
        print("fly fly")
class cow:
    pass
class ket(bird,cow):# muntitle-inheritance
    pass
