from tkinter import * #importing library and making a reference
import time

def testString():
    canvas.itemconfig(s0_label,fill = "red")
    canvas.after(5000,reset)

    

def reset():
    canvas.itemconfig(s0_label,fill = "blue")
    
    


root = Tk()


title  = Label(root , text=  "DFA for langauge that must start and end with the same symbol\nL = {{0,1}* | start and end with same symbol}\nTest your String below")
title.grid(row = 0)
entryString = Entry(root )
entryString.grid(row = 1 , column  = 0)
button = Button(root, text = "Submit",command=testString)
button.grid(row = 2 ,column =0)
canvas = Canvas(root, width =600 ,height = 500)
canvas.grid(row = 1 ,column = 1)

###########################################################################

state0 = canvas.create_oval(300,20,360,80)
state1 = canvas.create_oval(200,150,260,210)#accept state
accept_s1 = canvas.create_oval(190,140,270,220)# double cirle
state2 = canvas.create_oval(400,150,460,210)#accept state
accept_s2 = canvas.create_oval(390,140,470,220)#double circle
state3 = canvas.create_oval(200,330,260,390)
state4 = canvas.create_oval(400,330,460,390)
s0_label = canvas.create_text( 330,50 , text = "s0")
s1_label = canvas.create_text(230,180,text = "s1")
s2_label = canvas.create_text(430,180,text = "s2")
s3_label = canvas.create_text(230,360,text = "s3")
s4_label =canvas.create_text(430,360,text ="s4")


###################################################################

line1 = canvas.create_line(300,70, 230 ,135)#from state 0 to state 1
line2 = canvas.create_line(370,70,430,135)# from s0 to s2
line3 = canvas.create_line(210,225,210,325)#from s1 to s3
line4 = canvas.create_line(250,225,250,325)#from s3 to s1
line5 = canvas.create_line(410,225,410,325)#from s2 to s4
line6 = canvas.create_line(450,225,450,325)#from s4 to s2
line7 =canvas.create_line(190,150,80,160,190,210 ,smooth='true')#self loop on s1
line8 = canvas.create_line(470,150,580,160,470,210,smooth='true')#self loop on s2




root.mainloop()#runs the code





#///////////////////////////////////////////////////





#theLabel = Label(win,text = "this is too easy")

#widgets  , FRAME , LABEL , BUTTON , ENTRY

#label1 = Label(win,text = "username")
#label2 = Label(win,text = "password")
#entry1 = Entry(win)
#entry2 = Entry(win)

#label1.grid(row=0)
#label2.grid(row=1)

#entry1.grid(row=0,column=1 )
#entry2.grid(row=1,column=2,sticky = E)

#checkBox = Checkbutton(win,text = "keep me signed in")#check button
#checkBox.grid( columnspan =2)


#/////////////////////////////////////////////////////////////


#f =  Frame(win, width="500",height="500")

#def right(event):
 #   print("Right")

#def left(event):
 #   print("Right")


#f.bind("<Button-1>", left)
#f.bind("<Button-3>" , right)
#f.pack()