from tkinter import *
from tkinter import messagebox
def hello():
    messagebox.showinfo('hello','xin chao toi la Tam')
    
def left():
    print('Left')
    
def right():
    print('Right')
    
def top():
    print('Top')
    
def bottom():
    print('Bottom')
    
root = Tk()
'''
frame1=Frame(root)
frame1.pack()
btn1 = Button(frame1, text='click me',fg='white',bg='black',command=hello)
btn1.pack()# display

frame2=Frame(root)
frame2.pack(side=BOTTOM)
btn2 = Button(frame2, text='click here',fg='white',bg='black',command=hello)
btn2.pack()

label=Label(root,text='Hi',fg='white',bg='red')
label.pack(side=LEFT,fill=X)
label2=Label(root,text='Hey',fg='white',bg='red')
label2.pack(side=RIGHT,fill=Y)

label3=Label(root,text='Hey Hi',fg='white',bg='red')
label3.pack(fill=X)
'''
'''
label=Label(root,text='Alo',fg='white',bg='red')
label.grid(row=0, column=0, padx=2)
label2=Label(root,text='Alo',fg='white',bg='red')
label2.grid(row=0, column=1, padx=2)
label3=Label(root,text='Alo',fg='white',bg='red')
label3.grid(row=0, column=2, padx=2)
'''
logo=PhotoImage(file='pic.PNG')
label=Label(root,image=logo)
label.pack()

f=Frame(root)#we can set width=500,height=300 for frame
btn1=Button(f,text='Top',bg='red', fg='white', command=top)
btn1.grid(row=5,column=5)
btn2=Button(f,text='Left',bg='red', fg='white', command=left)
btn2.grid(row=6,column=4)
btn3=Button(f,text='Bottom',bg='red', fg='white', command=bottom)
btn3.grid(row=7,column=5)
btn4=Button(f,text='Right',bg='red', fg='white', command=right)
btn4.grid(row=6,column=6)

f.pack()
root.mainloop()# you have to do this