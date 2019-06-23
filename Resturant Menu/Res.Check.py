from tkinter import*
import random
import time;
import datetime as dt

root = Tk()
root.geometry('1920x1080+0+0')
root.title('Restarant Menu')
root.configure(background='black')

Tops = Frame(root, width=1350, height=100,bd=14, relief='raise')
Tops.pack(side=TOP)

f1= Frame(root, width=1200, height=1920, bd=8, relief='raise')
f1.pack(side=LEFT)

f2= Frame(root, width=700 , height=650,bd=8,relief='raise')
f2.pack(side=RIGHT)

f1a= Frame(f1, width=700, height=650,bd=8,relief='raise')
f1a.pack(side=TOP)

f2a= Frame(f1, width=700, height=650,bd=6,relief='raise')
f2a.pack(side=BOTTOM)


ft2= Frame(f2, width=900, height=600,bd=12,relief='raise')
ft2.pack(side=TOP)
fb2= Frame(f2, width=900, height=250,bd=16,relief='raise')
fb2.pack(side=BOTTOM)


f1aa= Frame(f1a, width=850, height=330,bd=8,relief='raise')
f1aa.pack(side=LEFT)
f1ab= Frame(f1a, width=700, height=330,bd=8,relief='raise')
f1ab.pack(side=RIGHT)

f2aa= Frame(f2a, width=700, height=100,bd=14,relief='raise')
f2aa.pack(side=RIGHT)
f2ab= Frame(f2a, width=700, height=100,bd=14,relief='raise')
f2ab.pack(side=LEFT)



lblInfo = Label(Tops , font=('arial',70,'bold'),text='   Restuarant Management System   ',bd=10)
lblInfo.grid(row=0,column=0)



root.mainloop()