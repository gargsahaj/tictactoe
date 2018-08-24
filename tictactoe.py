from tkinter import *
import random
def chkWin(sign):
	if (buttons[0]['text']==buttons[1]['text']==buttons[2]['text']==sign) or (buttons[3]['text']==buttons[4]['text']==buttons[5]['text']==sign) or \
	   (buttons[6]['text']==buttons[7]['text']==buttons[8]['text']==sign) or (buttons[0]['text']==buttons[3]['text']==buttons[6]['text']==sign) or \
	   (buttons[1]['text']==buttons[4]['text']==buttons[7]['text']==sign) or (buttons[2]['text']==buttons[5]['text']==buttons[8]['text']==sign) or \
	   (buttons[0]['text']==buttons[4]['text']==buttons[8]['text']==sign) or (buttons[2]['text']==buttons[4]['text']==buttons[6]['text']==sign):
	    if sign=='X':
	    	thelabel.configure(text="You Won!")
	    	for i in range(9):
	    		buttons[i].configure(state="disabled")
	    	return			
	    else:
	    	thelabel.configure(text="Comp Won!")
	    	for i in range(9):
	    		buttons[i].configure(state="disabled")
	    	return	
	elif len(number)==0:
	    	thelabel.configure(text="Draw!")    				
global turn
root = Tk()
buttons=[]
for j in range(3):
	for k in range(3):
		button=Button(root,height=5,width=5)
		button.grid(row=j,column=k)
		buttons.append(button)	
turn=0
global number
number=[0,1,2,3,4,5,6,7,8]
def clicked(num):
	global turn
	if turn==0:
		buttons[num].configure(text="X",state="disabled")
		number.remove(num)
		chkWin('X')
		turn=1
		if len(number)>=1:
			a=random.choice(number)
			buttons[a].configure(text="O",state="disabled")
			number.remove(a)
			chkWin('O')
			turn=0		
buttons[0].configure(command=lambda:clicked(0))
buttons[1].configure(command=lambda:clicked(1))
buttons[2].configure(command=lambda:clicked(2))
buttons[3].configure(command=lambda:clicked(3))
buttons[4].configure(command=lambda:clicked(4))
buttons[5].configure(command=lambda:clicked(5))
buttons[6].configure(command=lambda:clicked(6))
buttons[7].configure(command=lambda:clicked(7))
buttons[8].configure(command=lambda:clicked(8))
thelabel = Label(root)
thelabel.grid(row=3,columnspan=3)
root.mainloop()
