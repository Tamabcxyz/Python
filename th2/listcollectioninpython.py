a=["toi","la","tam"]
for item in a:
    print(item)
print(a[-1])
print(f"this is new line {a[1:3]}")
a.append("tran")
print(a)
a.insert(1,"khong")
print(a)
b=a
print(f"this is list b {b}")
b.append("0k")
print(f"this is list b {b}")
print(f"this is list a {a}")
c=b.copy()
c.pop()
print(f"this is list c {c}")
print(f"this is list b {b}")
print(f"this is list a {a}")