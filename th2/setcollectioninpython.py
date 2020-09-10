# set collection in python unordered and unindexed, but you can add items or remove them which writen with curly brackets
a={"toi","la","tam"}
print(a)
#add item into set collection
a.add("tran")
print(a)
#if you want add more items you can use update method
a.update(["this","is","update"])#it must be [] if you want add string 
print(a)
#remove and discard method to delete items in set collection
a.remove("is")# if items delete doesn't exist through error
a.discard("is")# if items delete doesn't exist not through error
print(a)
# merge two set 
set1={"hello","or hi"}
set2={"I'm Tam",}
set1=set1.union(set2)
print(set1)