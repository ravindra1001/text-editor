__author__ = 'ravindra'
from tkinter import *
from tkinter import filedialog
#global filename
filename = "default.txt"

def newFile():
    global filename
    filename = "default.txt"
    text.delete(0.0,END)



def saveFile():
    global filename
    fp=open(filename, 'w')
    t=text.get(0.0, END)
    fp.write(t.rstrip())
    text.delete(0.0, END)
    text.insert(0.0, t)
    fp.close()



def saveAs():
    global filename
    fp=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    t=text.get(0.0,END)
    filename = fp.name
    try:
        fp.write(t.rstrip())
    except:
        pass



def a():
    print("xyz")

def OpenFile():
    f= filedialog.askopenfilename()
    o=open(f,'r')
    t=o.read()
    text.delete(0.0,END)
    text.insert(0.0,t)
    o.close()


root=Tk()
text=Text(root)
root.title("My text editor")
root.minsize(width=450,height=500)
root.maxsize(width=450,height=500)

menubar = Menu(root)
root.config(menu=menubar)
filemenu = Menu(menubar)
filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="Open",command=OpenFile)
filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Save as...",command=saveAs)
filemenu.add_separator()
menubar.add_cascade(label="File",menu=filemenu)

Editmenu=Menu(menubar)
menubar.add_cascade(label="Edit",menu=Editmenu)
Editmenu.add_command(label="Cut",command=a)
Editmenu.add_command(label="Copy",command=a)
Editmenu.add_command(label="Paste",command=a)

view=Menu(menubar)
menubar.add_cascade(label="View",menu=view)
view.add_command(label="View line no...",command=a)

exitmenu=Menu(menubar)
menubar.add_cascade(label="Exit",menu=exitmenu)
exitmenu.add_command(label="Exit",command=root.quit)


text.pack(side=LEFT,fill= BOTH)

scr=Scrollbar(root)
scr.pack(side=RIGHT, fill=Y)
text.config(yscrollcommand=scr.set)
scr.config(command=text.yview)

status=Label(root,text="prepairing",bd=1, relief=SUNKEN)
status.pack(side=BOTTOM, fill=X)

root.mainloop()