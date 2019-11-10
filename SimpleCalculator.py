import tkinter
from tkinter import *
def click(event):
	global scvalue
	text=event.widget.cget("text")
	print(text)
	if text=="=":
		if scvalue.get().isdigit():
			value=int(scvalue.get())
		else:
			value=eval(screen.get())

		scvalue.set(value)
		screen.update()	
	elif text=="C":
		scvalue.set("")
		screen.update()
	else:
		scvalue.set(scvalue.get()+text)
		screen.update()
		
		
root=Tk()
root.geometry('300x440')
root.title("Calculator By Aakanksha")
root.resizable(0,0)

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue, font="lucida 20 bold")
screen.pack(fill=X, ipadx=10, pady=5, padx=5)



f1=Frame(root,bg="grey")
b1=Button(f1,text="9",font="lucida 15 bold")
b1.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b1.bind("<Button-1>",click)

b2=Button(f1,text="8",font="lucida 15 bold")
b2.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b2.bind("<Button-1>",click)

b3=Button(f1,text="7",font="lucida 15 bold")
b3.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b3.bind("<Button-1>",click)
f1.pack(fill=BOTH)


f2=Frame(root,bg="grey")
b4=Button(f2,text="6",font="lucida 15 bold")
b4.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b4.bind("<Button-1>",click)

b5=Button(f2,text="5",font="lucida 15 bold")
b5.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b5.bind("<Button-1>",click)

b6=Button(f2,text="4",font="lucida 15 bold")
b6.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b6.bind("<Button-1>",click)
f2.pack(fill=BOTH)



f3=Frame(root,bg="grey")
b7=Button(f3,text="3",font="lucida 15 bold")
b7.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b7.bind("<Button-1>",click)

b8=Button(f3,text="2",font="lucida 15 bold")
b8.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b8.bind("<Button-1>",click)

b9=Button(f3,text="1",font="lucida 15 bold")
b9.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b9.bind("<Button-1>",click)
f3.pack(fill=BOTH)




f4=Frame(root,bg="grey")
b10=Button(f4,text="0",font="lucida 15 bold")
b10.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b10.bind("<Button-1>",click)

b11=Button(f4,text="-",font="lucida 15 bold")
b11.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b11.bind("<Button-1>",click)

b12=Button(f4,text="+",font="lucida 15 bold")
b12.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b12.bind("<Button-1>",click)
f4.pack(fill=BOTH)




f5=Frame(root,bg="grey")
b13=Button(f5,text="*",font="lucida 15 bold")
b13.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b13.bind("<Button-1>",click)

b14=Button(f5,text="/",font="lucida 15 bold")
b14.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b14.bind("<Button-1>",click)

b15=Button(f5,text="%",font="lucida 15 bold")
b15.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b15.bind("<Button-1>",click)
f5.pack(fill=BOTH)


f6=Frame(root,bg="grey")
b16=Button(f6,text=".",font="lucida 15 bold")
b16.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b16.bind("<Button-1>",click)

b17=Button(f6,text="C",font="lucida 15 bold")
b17.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b17.bind("<Button-1>",click)

b18=Button(f6,text="=",font="lucida 15 bold")
b18.pack(side=LEFT,ipadx=14,padx=20,pady=12)
b18.bind("<Button-1>",click)
f6.pack(fill=BOTH)

root.mainloop()