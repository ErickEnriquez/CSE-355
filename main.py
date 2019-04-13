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
line7 = canvas.create_line(190,150,80,160,190,210 ,smooth='true')#self loop on s1
line8 = canvas.create_line(470,150,580,160,470,210,smooth='true')#self loop on s2
line9 = canvas.create_line(210,390,230,470,250,390,smooth='true')#self loop on s3
line10 = canvas.create_line(410,390,430,470,450,390,smooth='true')#self loop on s4

######################################################################

input1 = canvas.create_text(260,90,text="0")#s0 input 0 to s1
input2 = canvas.create_text(410,90,text ="1")#s0 input to s2
input3 = canvas.create_text(120,170,text ='0')#s1 input 0 self loop
input4 = canvas.create_text(540,170,text = '1')#s2's input 1 self loop
input5 = canvas.create_text(200,280,text = '1')#s1's input 1 to s3
input6 = canvas.create_text(460,280,text ='0')#s2's input 0 to s4
input7 = canvas.create_text(260,280,text ='0')#s3's input 0 to s1
input8 = canvas.create_text(400,280,text='1')#s4's input 1 to s2
input9 = canvas.create_text(230,450,text ='1')#s3's input 1 self loop
input10 = canvas.create_text(430,450,text='0')#s4's input 0 self loop

root.mainloop()#runs the application
