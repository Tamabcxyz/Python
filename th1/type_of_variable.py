a=1
b=2.4
c=2+1j
print("type of a is ",type(a))
print("type of b is ", type(b))
print("type of c is ", type(c))
print(c," is number complex ",isinstance(c,complex))
# list in python
lista=[1,1.2,'chao cau']
lista[2]="hello"
print(lista[0],lista[1],lista[2])
# with cuple
# note: cannot be change value in cuple
listb=(1,1.2,'chao cau')
# listb[2]="xin chao"
print("This is cuple: ",listb[0],listb[1],listb[2])
# string in python
vd="xin chao day la chuoi cua toi"
print(vd)
print("[5:10]",vd[5:10])#kq:hao da
# note: cannot be change value in string
#vd[5]='s'
print(vd)
print(type(vd))
# python set
a={5,3,4,1,2}
#print(a[1]) it's not work
print("a=",a)
print(type(a))
b={1,2,2,2,3,3,3,4,5}
print(b)
