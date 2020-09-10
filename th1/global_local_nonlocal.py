x="global"
def f():
    print("inside f",x)
f()
print("outside f",x)
#other
x=3
def f():
    global x
    x=x+1
    print("inside f",x)
f()
print("outside f",x)
#other about local variable
x=3
def f():
    x=1
    x=x+1
    print("inside f",x)
f()
print("outside f",x)
