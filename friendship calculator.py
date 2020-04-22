from tkinter import *
import tkinter.messagebox
master = Tk()
master.geometry('750x620')
master.configure(bg='VioletRed1')
master.title("Friendship Calculator")

def clear():
  output.delete(first=0,last=10000000)
  name1.delete(first=0,last=10000000)
  name2.delete(first=0,last=10000000)

def cancel():
  output.delete(first=0,last=10000000)
  

def calculation():
  a=str(name1.get())
  b=str(name2.get())
  c=list(set(a)&set(b))
  l=len(c)

  z=[]
  if l==1 or l==2:
    f="20%"
    z.append(f)
  elif l==3 or l==4:
    f="40%"
    z.append(f)
  elif l==5 or l==6:
    f="60%"
    z.append(f)
  elif l==7 or l==8:
    f="80%"
    z.append(f)
  else:
    f="100%"
    z.append(f)

  y= ','.join(z)
  output.insert(0,y)
  tkinter.messagebox.showinfo("Info","The result of this friendship test is based on your name")


output = Entry(master,font=("Courier New",100,"bold"),bg="RosyBrown3")
output.place(x=320,y=70,width=350,height=270)


name1=Entry(master,font=("Courier New",12,"bold"),width=50,bd=15,bg="powder blue")
name1.place(x=200,y=350)

name2=Entry(master,font=("Courier New",12,"bold"),width=50,bd=15,bg="powder blue")
name2.place(x=200,y=450)

lebel= Label(master,font=("Courier New",25,"bold"),bg="VioletRed1",bd=15,text="Name 1")
lebel.place(x=15,y=330)

lebel1= Label(master,font=("Courier New",25,"bold"),bg="VioletRed1",bd=15,text="Name 2")
lebel1.place(x=15,y=430)

lebel4= Label(master,font=("Courier New",20,"bold"),bg="VioletRed1",bd=15,text="Friendship Calculator")
lebel4.place(x=290,y=15)


photo = PhotoImage(file = "/root/Desktop/hi/A.LOVE CALCULATOR/9.gif")
label =Label(image = photo)
label.place(x=2,y=10)

button1 =Button(master,text=" CALCULATE ",command=calculation, font=("Courier New", 25),bd=10)
button1.place(x=470,y=530)

button1 =Button(master,text=" CANCEL ",command=cancel, font=("Courier New", 25),bd=10)
button1.place(x=265,y=530)
 
button1 =Button(master,text=" CLEAR ",command=clear, font=("Courier New", 25),bd=10)
button1.place(x=80,y=530)

mainloop() 
