def addition(a,b):
    #print(a+b)
    a=5
    b=5
    return a+b
def myfunction(*temp):
    print("hello "+temp[1])
a=3
b=4   
c=addition(a,b)
print(a)
print(b)
print(c)
# you can add more parametter if you want because you use *temp in your function it can receive tuple of parametter
myfunction("a","b","c")
def my_function(**kid):
    print("His last name is " + kid["lname"])
# receive items dictionary 
my_function(fname = "Tobias", lname = "Refsnes")
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
