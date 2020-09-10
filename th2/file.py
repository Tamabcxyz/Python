f=open("test.txt","rt")
print(f.read())
f.close()
#print(f.read(5))# i want to read five character
#print(f.readline())# i want to rea a line in file

t=open("test.txt","a")# with a you can append at the end of files
t.write("more content to file test")
t.close()
f=open("test.txt","r")
print(f.read())
f.close()
# to create file we can use f=open("test.txt","x") 
# to delete a files we must import os and use os.remove(namefile)
# if you want to delete a folde os.rmdir(namefolder) 