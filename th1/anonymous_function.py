a=lambda argument:argument*2#it's not inline
print(a(2))#call anonymous function
#other with list
list1=[1,2,3,4,5,6,7,6,4,8,9]
new_list=list(filter(lambda s:s%2==0,list1))
print(new_list)
#other with map
list2=[1,2,3,4,5,6,7,6,4,8,9]
new=list(map(lambda x:x*2,list2))
print(new)
