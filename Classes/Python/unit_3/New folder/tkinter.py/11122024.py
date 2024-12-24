import tkinter
from tkinter import*
win=Tk()
win.title("Tkinter Canvas Widget Demonstration")
win.geometry("400x250")
cv=Canvas(win,bg="orange",height="250",width="400")
cv.pack()
username=Label(win,text='Enter your Username: ').place(x=50,y=50)
password=Label(win,text='Enter your password!').place(x=50,y=90)

submitbutton=Button(win,text='sumbit',activebackground="green",activeforeground='blue').place(x=50,y=120)
e1=Entry(win,width=20).place(x=200,y=50)
e2=Entry(win,width=20).place(x=200,y=90)
win.mainloop()

