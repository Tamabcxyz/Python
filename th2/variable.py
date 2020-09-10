a=5
b="abc"
c='acb'
print(a)
print(b)
print(c)
print("this is a "+str(a)+"\nthis is b "+b+"\nthis is c "+c)
print(type(a))
print(type(b))
print(type(c))
x=range(6)
print(x)
for item in x:
    print(item)
y={"name":"Tran Minh Tam","age":24}
print(y)
#d=dict(y)
for key,item in y.items():
    print(str(key)+":"+str(item))
animals = {'ralph': ('dog', 160101),'marley': ('dog', 160102),'sam': ('cat', 160103),'bones': ('dog', 160104),'bella': ('cat', 160105),'max': ('dog', 160106),'daisy': ('cat', 160107),'angel': ('cat', 160108),'luna': ('cat', 160109),'buddy': ('dog', 160110),'coco': ('dog', 160111)}
for name, animal in animals.items():
    type_animal,count_animal=animal
    print(f"The {type_animal} {name} has the numbers {count_animal}")