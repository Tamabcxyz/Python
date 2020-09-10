#A dictionary is a collection unordered can changeable, index. In python dictionary are written with curly brackets
#the have keys and values
a={"name":"Tran Minh Tam", "age":22}
print(a)
for x in a.values():
    print(x)
for x in a.keys():
    print(x)
for x,y in a.items():
    print(f"a have key {x} values is {y}")
#add item you can write below
a["address"]="VL_CT"
print(a)