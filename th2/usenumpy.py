import numpy
a=numpy.array([1,2,3,4,5])
print(a)
print(type(a))
print(numpy.__version__)
b=numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# we have 2 way to print elements 
#fisrt one
print("first way")
for x in b:
    for y in x:
        for z in y:
            print(z)
print("another way")
for x in numpy.nditer(b):
    print(x)