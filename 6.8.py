import tkinter as tk
root = tk.Tk()
v= tk.IntVar()
v.set(1) #initializing the choice, i.e.Python
language=[("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)]
def ShowChoice():
  print(v.get())
tk.Label(root,text="""Choose your favourite programming language:""", justify=tk.LEFT, padx=20).pack()
for val, language in enumerate(language):
  tk.Radiobutton(root, text=language,padx=20,variable=v,command=ShowChoice,value=val).pack(anchor=tk.W)
  root.mainloop()
 10  5b.py 
@@ -0,0 +1,10 @@
import tkinter as tk
root = tk.Tk()
v= tk.IntVar()
v.set(1) #initializing the choice, i.e.Python
language=[("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)]
def ShowChoice():
  print(v.get())
tk.Label(root,text="""Choose your favourite programming language:""", justify=tk.LEFT, padx=20).pack()
for val, language in enumerate(language):
  tk.Radiobutton(root,text=language,indicatoron=0,width=20,variable=v,command=ShowChoice,value=val).pack(anchor=tk.W)
 48  6.py 
@@ -1,18 +1,30 @@
import sys
import os
def file_read_from_tail(fname,lines):
    bufsize=8192
    fsize=os.stat(fname).st_size
    iter=0
    with open(fname) as f:
        if bufsize>fsize:
            bufsize=fsize-1
            data =[]
            while True:
                iter+=1
                f.seek(fsize-bufsize*iter)
                data.extend(f.readlines())
                if len(data)>=lines or f.tell()==0:
                    print(''.join(data[-lines:]))
                    break
file_read_from_tail('text.txt',2)
from tkinter import*
def NewFile():
  print("New File!")
def OpenFile():
  print("Open File!")
def ExitFile():
  print("Exit File!")
def TextInsert():
  print("Text Insert!")
def PictureInsert():
  print("Picture Insert!")
def About():
  print("This is a simple example of a menu")
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)
filemenu=Menu(menu)
menu.add_cascade(label="Insert",menu=filemenu)
filemenu.add_command(label="Text", command=TextInsert)
filemenu.add_command(label="Picture", command=PictureInsert)
helpmenu=Menu(menu)
menu.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="About...",command=About)
mainloop()
