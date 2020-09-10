'''
#my sign draw
from tkinter import *

canvas_width = 500
canvas_height = 200

def paint( event ):
   col = "red"
   x1, y1 = ( event.x - 1 ), ( event.y - 1 )
   x2, y2 = ( event.x + 1 ), ( event.y + 1 )
   w.create_oval( x1, y1, x2, y2, fill = col )

master = Tk()
master.title( "Painting using Ovals" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)# expand=YES if have event follow event otherwise use old, BOTH fill coordinates x and y
w.bind( "<B1-Motion>", paint )# <B1-Motion> event mouse is moved

message = Label( master, text = "Press and Drag the mouse to draw" )
message.pack( side = BOTTOM )
    
mainloop()
'''
'''
# test click and key but it don't catch ctrl,shift....
from tkinter import *

root = Tk()

def key(event):
    print (f"pressed {repr(event.char)}")

def callback(event):
    frame.focus_set()
    print (f"clicked at {event.x, event.y}") 

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
'''
'''
# draw triangle
from tkinter import *
h=200
w=200
root=Tk()
root.title("Draw triangle")
c=Canvas(root,width=w,height=h)
c.create_polygon(0,0,w,h/2,0,h)
c.pack()
root.mainloop()
'''
'''
#draw star
from tkinter import *

canvas_width = 200
canvas_height =200
python_green = "red"

master = Tk()

w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

points = [100, 140, 110, 110, 140, 100, 110, 90, 100, 60, 90, 90, 60, 100, 90, 110]

w.create_polygon(points, outline=python_green, fill='yellow', width=3)

mainloop()
'''
'''
# draw icon
from tkinter import *

canvas_width = 300
canvas_height =80

master = Tk()
canvas = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
canvas.pack()

bitmaps = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
nsteps = len(bitmaps)
step_x = int(canvas_width / nsteps)

for i in range(0, nsteps):
   canvas.create_bitmap((i+1)*step_x - step_x/2,50, bitmap=bitmaps[i])

mainloop()
'''
'''
# add image
from tkinter import *

canvas_width = 300
canvas_height =300

master = Tk()

canvas = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
canvas.pack()

img = PhotoImage(file="pic.PNG")
canvas.create_image(20,20, anchor=NW, image=img)

mainloop()
'''
'''
# table cheese
from tkinter import *

def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#476042")


master = Tk()
canvas_width = 500
canvas_height = 500 
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

checkered(w,50)

mainloop()
'''
'''
from tkinter import *

def show_values():
    print (w1.get(), w2.get())

master = Tk()
w1 = Scale(master, from_=0, to=42, tickinterval=8)
w1.set(29)# values start
w1.pack()
w2 = Scale(master, from_=0, to=200, length=400,tickinterval=50, orient=HORIZONTAL)
w2.set(23)
w2.pack()
Button(master, text='Show', command=show_values).pack()

mainloop()
'''
'''
#show dialog
import tkinter as tk
from tkinter import messagebox as mb

def answer():
    mb.showerror("Answer", "Sorry, no answer available")

def callback():
    if mb.askyesno('Verify', 'Really quit?'):
        mb.showwarning('Yes', 'Not yet implemented')
    else:
        mb.showinfo('No', 'Quit has been cancelled')

tk.Button(text='Quit', command=callback).pack(fill=tk.X)
tk.Button(text='Answer', command=answer).pack(fill=tk.X)
tk.mainloop()
'''
'''
#choose file
import tkinter as tk
from tkinter import filedialog as fd 

def callback():
    name= fd.askopenfilename() 
    print(name)
    
errmsg = 'Error!'
tk.Button(text='File Open', 
       command=callback).pack(fill=tk.X)
tk.mainloop()
'''
import tkinter as tk
from tkinter.colorchooser import askcolor                  

def callback():
    result = askcolor(color="#6A9662", 
                      title = "Bernd's Colour Chooser") 
    print(result)
    
root = tk.Tk()
tk.Button(root, 
          text='Choose Color', 
          fg="darkgreen", 
          command=callback).pack(side=tk.LEFT, padx=10)
tk.Button(text='Quit', 
          command=root.quit,
          fg="red").pack(side=tk.LEFT, padx=10)
tk.mainloop()