temp='my boss'
temp2=3
temp3="my boss"
temp4="ong chu"
print(f"hello {temp}")
print(f"hello {temp2}")
print(f"hello {temp3}")
print(f'hello {temp4}')
print(f'hello {temp}')
a=500
b=500
c=a+b
print(f"if I have {a} I addition with {b} I will have total is {c}")
# if you want use math library in python You have to import math
import math
arr={1,2,3,4,5}
arr1=[1,2,3,4]
arr2=(1,2,3)
total=math.fsum(arr)
print(f"I use method SUM in python I get total is {total}")
print(f"I use method SUM in python I get total is {math.fsum(arr1)}")
print(f"I use method SUM in python I get total is {math.fsum(arr2)}")
# this is other way to create and use a array
array={
    1:  'I',
    2:  'have',
    3:  "an",
    4:  'array'
    }
dictA = {
    1,2,3
}
k=sum(dictA)
print(k)
# other aspect
d="1"
e="2"
kq=float(d)+float(e)
kq1=float(d+e)
print(kq)
print(kq1-1)
# different
n="3"
m="4"
print(f"tong n va m la: {int(n)+int(m)} \n")
# other
user = "Sammy"
lines = 50
print(f"Congratulations {user}! You just wrote {lines} lines of code.")
print("Congratulations, " + user + "! You just wrote " + str(lines) + " lines of code.")
#other
x='chao ban'
y="minh la tam"
z= x+" "+y
print(z)
#other
p=10
q=2
print(str(p)+str(q))
#other
lists=["1","2","3"]
print(tuple(lists))
lists1=["1","2","3"]
print(list(lists1))
lists2=[1,2,3,4,5]
print(list(lists2))
#other
print("*"*10)
a=[1,2,[1,2,"hello",["chao",3,4]],7,4]
print(a)
print(a[2][2])
print(a[2][3][0])
x=[1,2,3]
x=x+[6,5,9]
print(x)
































