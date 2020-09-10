class Parrot:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,sing="o o o..."):
        return "{} sing {}".format(self.name,sing)
a=Parrot("pig",23)
b=Parrot("cow",34)
print(a.name)
print(a.age)
print(a.sing('a b c'))
print(b.sing())
