#attention tuple is unchangeable
a=("toi","la","tam")
print(f"{a[0]},{a[1]},{a[2]}")
#a.append("tran") it does't work
#print(f"{a[0]},{a[1]},{a[2]}")
b=list(a)# convert tuple to list
b.append("tran")
a=tuple(b)
print(a)