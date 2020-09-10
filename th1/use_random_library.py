import random
lista=['a','b','c','d','e']
print(random.choice(lista))
a=random.randrange(10,20)
print(a)
random.shuffle(lista)
print(lista)
print(round(random.random()*10))
