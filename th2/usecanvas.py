from tkinter import *
from tkinter import messagebox

tk = Tk()
cas = Canvas(tk, width=1000, height=1000)
cas.create_line(100,234,423,423, fill='red')
cas.create_rectangle(100,100,200,200,fill='black')
cas.create_oval(50,50,100,100)
cas.pack()
tk.mainloop()# windows form alway use mainloop 