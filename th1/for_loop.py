arr=[1,2,3,4,5]
sum=1
for i in arr:
    sum+=i
print(sum)
for i in range(1,10,2):
    print(i)
a=["jonh","jack","lina","eva"]
for i in range(len(a)):
    print("this is ",a[i])
    if a[i]=="lina":
        break
else: print("stop loop")
