class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        x=self.x
        y=self.y
        return "({0},{1})" .format(x,y)
    def __add__(self,self1):# if is __add__ then you  can print(Point+Point) else no run
        x=self.x+self1.x
        y=self.y+self1.y
        return Point(x,y)
a=Point(2,3)
b=Point(4,5)
print(a.__str__()+b.__str__())
print(a+b)
