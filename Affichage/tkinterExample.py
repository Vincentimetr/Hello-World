from tkinter import *

window=Tk()
window.title("windowName")
window.configure(background="black")

#Insert Image
photo=PhotoImage(file="E:/Drive/PYTHON/tkinterExample.gif")
Label(window,image=photo,bg="black").grid(row=0,column=0,sticky=W)

#Insert Text
Label(window,text="type text",bg="black",fg="white",font="none 12 bold").grid(row=1,column=0,sticky=W)

#Insert TextBox
Text(window,width=10,height=10,background="white").grid(row=2,column=0,sticky=W)

#Text EntryBox
textEntry=Entry(window,width=20,bg="black",fg="red")
textEntry.grid(row=3,column=0,sticky=W)

#Insert case
Label(window,width=1,height=1,bg="green").grid(row=6,column=0,sticky=W)

#Button
def button1():
    return textEntry.get()
Button(window,text="Submit",width=5,command=button1).grid(row=4,column=0,sticky=W)
def close():
    window.destroy()
    return
Button(window,text="EXIT",width=5,command=close).grid(row=5,column=0,sticky=W)

Button(window,width=2,bg="red",command=close).grid(row=7,column=0,sticky=W)

window.mainloop()