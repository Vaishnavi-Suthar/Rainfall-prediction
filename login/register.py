from os import name
from tkinter import *
from tkinter import messagebox
import ast

window=Tk()
window.title('Ragistration')
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False,False)

def signup():
    username=user.get() 
    password=code.get()
    conform_password=conform_code.get()

    if password==conform_password: 
        try:
            file=open(r'D:\sem_6\project\pr_2\login\dataseet.txt','r+')
            d=file.read()
            r=ast.literal_eval(d)

            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file=open(r'D:\sem_6\project\pr_2\login\dataseet.txt','w')
            w=file.write(str(r))

            messagebox.showinfo('Signup','Sucessfully sign up')

        except:
            file=open(r'D:\sem_6\project\pr_2\login\dataseet.txt','w')
            pp=str({'Username':'password'})
            file.write(pp)
            file.close()

    else:
        messagebox.showerror('Invalid','Both Password should match')



       
        

   


img = PhotoImage(file=r"D:\sem_6\project\pr_2\login\register.png")
Label(window,image=img,bg='white').place(x=50,y=100)

frame=Frame(window,width=350,height=390,bg="white")
frame.place(x=480,y=50)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=120,y=5)

## Username

def on_enter(e):
    user.delete(0,'end')
    
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

## Password

def on_enter(e):
    code.delete(0,'end')
    
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

## Conform Password

def on_enter(e):
    conform_code.delete(0,'end')
    
def on_leave(e):
    if name=='':
        conform_code.insert(0,'Conform Password')

conform_code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
conform_code.place(x=30,y=220)
conform_code.insert(0,'Conform Password')
conform_code.bind('<FocusIn>',on_enter)
conform_code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

##  Button

Button(frame, width=30, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0 ,command=signup). place (x=35,y=280) 
label=Label (frame, text="I have an account", fg='black', bg='white', font=('Microsoft YaHei UI Light',9)) 
label.place(x=90,y=340)

sign_up=Button(frame,width=6,text="Sign in", border=0, bg='white', cursor='hand2', fg='#57a1f8') 
sign_up.place(x=200,y=333)

window.mainloop()