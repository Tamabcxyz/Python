#with open("test.txt",'w',encoding = 'utf-8') as f:
#    f.write("this is test file")
# if you have with you don'n need to call f.close()

'''f = open("test.txt",'r',encoding = 'utf-8')
print(f.read())
f.close()'''

'''with open("test.txt",'a') as file:
    file.write("file after append new string")'''

#other
import os
print(os.getcwd())
print(os.getcwdb())

#change dir in python use chdir()
#other
print(os.listdir())

# other I try exception file by way call file not exist
try:
    f=open("abc.txt",'r',encoding='utf-8')
    print(file.read())
    f.close()
except:
    print("loi!")
finally: print("this is finally")
