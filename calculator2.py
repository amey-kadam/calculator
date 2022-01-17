from tkinter import *
from tkinter import messagebox
from PIL import  Image,ImageTk
from decimal import *


win = Tk()
win.geometry('300x380')
win.title("calculator")
win.iconbitmap("C:\\Users\\ameyp\\Downloads\\Calculator12.ico")
win.configure(bg="#1C1C1C")
text = Entry(win,font=("calibri",22), bg='black',foreground ='white', bd=0)
text.place(x=0,y=0,height=82)

def addToText(n):
    text.insert(END,n)
    
def calculate():
    result = eval(text.get())
    text.delete(0,END)
    text.insert(0,result)
    
def clear():
    text.delete(0,END)

def backspace():
    text.delete(len(text.get())-1)

def mod_clicked():
    pos = len(text.get())
    text.insert(pos, '%')    
       

#btn1 to btn3
btn1=Button(win,text="1",width=10,height=4,command=lambda:addToText("1"),bg='#1C1C1C',foreground ='white', bd='0')
btn1.place(x=10, y=80)
btn2=Button(win,text="2",width=10,height=4,command=lambda:addToText("2"),bg='#1C1C1C',foreground ='white', bd='0')
btn2.place(x=84,y=80)
btn3=Button(win,text="3",width=10,height=4,command=lambda:addToText("3"),bg='#1C1C1C',foreground ='white', bd='0')
btn3.place(x=155,y=80)

#btn4 to btn6
btn4=Button(win,text="4",width=10,height=4,command=lambda:addToText("4"),bg='#1C1C1C',foreground ='white', bd='0')
btn4.place(x=10,y=135)
btn5=Button(win,text="5",width=10,height=4,command=lambda:addToText("5"),bg='#1C1C1C',foreground ='white', bd='0')
btn5.place(x=84, y=135)
btn6=Button(win,text="6",width=10,height=4,command=lambda:addToText("6"),bg='#1C1C1C',foreground ='white', bd='0')
btn6.place(x=155,y=135)

#btn7 to btn9
btn7=Button(win,text="7",width=10,height=4,command=lambda:addToText("7"),bg='#1C1C1C',foreground ='white', bd='0')
btn7.place(x=10,y=190)
btn8=Button(win,text="8",width=10,height=4,command=lambda:addToText("8"),bg='#1C1C1C',foreground ='white', bd='0')
btn8.place(x=84,y=190)
btn9=Button(win,text="9",width=10,height=4,command=lambda:addToText("9"),bg='#1C1C1C',foreground ='white', bd='0')
btn9.place(x=155,y=190)

#btn0,00,=
btn10=Button(win,text="00",width=10,height=4,command=lambda:addToText("00"),bg='#1C1C1C',foreground ='white', bd='0')
btn10.place(x=10,y=245)
btn11=Button(win,text="0",width=10,height=4,command=lambda:addToText("0"),bg='#1C1C1C',foreground ='white', bd='0')
btn11.place(x=84, y=245)
btn12=Button(win,text=".",width=10,height=4,command=lambda:addToText("."),bg='#1C1C1C',foreground ='white', bd='0')
btn12.place(x=155,y=245)

#operators
btn13=Button(win,text="+",width=10,height=4,command=lambda:addToText("+"),bg='#1C1C1C',foreground ='darkturquoise', bd='0')
btn13.place(x=217,y=80)
btn14=Button(win,text="-",width=10,height=4,command=lambda:addToText("-"),bg='#1C1C1C',foreground ='darkturquoise', bd='0')
btn14.place(x=217,y=135)
btn15=Button(win,text="x",width=10,height=4,command=lambda:addToText("*"),bg='#1C1C1C',foreground ='darkturquoise', bd='0')
btn15.place(x=217,y=190)
btn16=Button(win,text="/",width=10,height=4,command=lambda:addToText("/"),bg='#1C1C1C',foreground ='darkturquoise', bd='0')
btn16.place(x=217,y=245)

#extras
btn17=Button(win,text="=",width=10,height=4,command=lambda:calculate(),bg='#1C1C1C',foreground ='darkturquoise', bd='0')
btn17.place(x=10, y=300)
btn18=Button(win,text="c",width=10,height=4,command=lambda:clear(),bg='#1C1C1C',foreground ='darkturquoise', bd='0')
btn18.place(x=84, y=300)
btn19=Button(win,text="bck",width=10,height=4,command=lambda:backspace(),bg='#1C1C1C',foreground ='darkturquoise', bd='0')
btn19.place(x=155, y=300)
btn20=Button(win,text="%",width=10,height=4,command=lambda:mod_clicked("%"),bg='#1C1C1C',foreground ='darkturquoise', bd='0')
btn20.place(x=217, y=300)


lbl=Label(win,text="",background='#1C1C1C') 
lbl.place(x=292,y=80)
lbl2=Label(win,text="",background='#1C1C1C',width=1)
lbl2.place(x=0,y=80)

win.mainloop()
