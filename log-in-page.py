from tkinter import *
t=Tk()
t.configure(background="grey")
t.geometry('600x600')
t.title('LOGIN FORM')

l=Label(t,text="LOGIN FORM",fg='black',font=30)
l.pack()
l.place(y=15,x=250)
u=Label(t,text="Username  :",fg='white',bg='grey',font=30)
u.pack()
u.place(x=150,y=70)
e=Entry(t,width=30)
e.pack()
e.place(x=250,y=72)
p=Label(t,text="Password  :",fg='white',bg='grey',font=30)
p.pack()
p.place(x=150,y=100)
m=Entry(t,width=30)
m.pack()
m.place(x=250,y=102)
def display():
    g=Label(t,text="welcome "+e.get())
    g.pack()
    g.place(y=170,x=250)
b= Button(t,text="submit",command=display)
b.pack()
b.place(y=135,x=250)


t.mainloop()