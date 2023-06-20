from tkinter import *

t = Tk()
t.configure(background='black')
t.resizable(False,False)
t.geometry('500x600')
t.title('calculator')

l=Label(t,text="welcome",bg='blue',fg='white',font=30)
l.pack()
l.place(x=20,y=10)

e = Entry(t,width=50)
e.pack() 

def display():
    g=Label(t,text="welcome"+e.get())
    g.pack()
    

b= Button(t,text="click here",command=display)
b.pack()

t.mainloop()