from tkinter import *
master = Tk()
master.geometry('750x620')
master.configure(bg='VioletRed1')
master.title("Friendship Calculator")


name1=Entry(master,font=("Courier New",12,"bold"),width=50,bd=15,bg="powder blue")
name1.place(x=200,y=350)

name2=Entry(master,font=("Courier New",12,"bold"),width=50,bd=15,bg="powder blue")
name2.place(x=200,y=450)

output = Entry(master,font=("Courier New",100,"bold"),bg="RosyBrown3")
output.place(x=320,y=70,width=350,height=270)

lebel= Label(master,font=("Courier New",25,"bold"),bg="VioletRed1",bd=15,text="Name 1")
lebel.place(x=15,y=330)

lebel1= Label(master,font=("Courier New",25,"bold"),bg="VioletRed1",bd=15,text="Name 2")
lebel1.place(x=15,y=430)

lebel2= Label(master,font=("Courier New",20,"bold"),bg="VioletRed1",bd=15,text="Friendship Calculator")
lebel2.place(x=290,y=15)


photo = PhotoImage(file = "/root/Documents/1.gif")
label =Label(image = photo)
label.place(x=2,y=10)


mainloop() 
