from tkinter import * #importing library and making a reference
import time


def getString():
   s  = entryString.get()#get the string user enters
   string = list(s)#cast our string into a list
   for i in string:
       if i != '1'  and i != '0':
           quit()#quit the program
   state = 's0'
   check(string,state)
   

   
def check(string,state):#get string contents recursively
    if not string:#if list is empty
        Qfinal(state)
        return
   
    symbol = string.pop(0)#pop the symbol from the list
    state = transitionFuntion(state,symbol)#get our new state
    canvas.after(1000,reset,1)#reset the gui 
    canvas.after(1000,check,string ,state)#recursively call check again
   


def transitionFuntion(state , symbol):
    if(state == 's0' and symbol == '0' ):
        canvas.itemconfig(input1 ,fill = 'red')
        return 's1'
    elif (state == 's0' and symbol == '1'):
        canvas.itemconfig(input2 ,fill = 'red')
        return 's2'
    elif (state == 's1' and symbol == '0'):
        canvas.itemconfig(input3,fill = 'red')
        return 's1'
    elif(state == 's1' and symbol == '1'):
        canvas.itemconfig(input5,fill = 'red')
        return 's3'
    elif (state == 's2' and symbol == '0'):
        canvas.itemconfig(input6,fill = 'red')
        return 's4'
    elif (state == 's2' and symbol == '1'):
        canvas.itemconfig(input4,fill = 'red')
        return 's2'
    elif (state == 's3' and symbol == '0'):
        canvas.itemconfig(input7,fill = 'red')
        return 's1'
    elif (state == 's3' and symbol == '1'):
        canvas.itemconfig(input9,fill = 'red')
        return 's3'
    elif (state == 's4' and symbol == '0'):
        canvas.itemconfig(input10,fill = 'red')
        return 's4'
    elif (state == 's4' and symbol == '1'):
        canvas.itemconfig(input8,fill = 'red')
        return 's2'

def reset(i):#resets the GUI
    if i == 0:
        return
    canvas.itemconfig(s0_label,fill= 'black')
    canvas.itemconfig(state0,outline = 'black')
    canvas.itemconfig(input1,fill = 'black')
    canvas.itemconfig(input2,fill = 'black')
    canvas.itemconfig(input3,fill ='black')
    canvas.itemconfig(input4,fill = 'black')
    canvas.itemconfig(input5,fill = 'black')
    canvas.itemconfig(input6,fill = 'black')
    canvas.itemconfig(input7,fill ='black')
    canvas.itemconfig(input8,fill = 'black')
    canvas.itemconfig(input9,fill ='black')
    canvas.itemconfig(input10,fill ='black')
    canvas.after(0,reset,0)

def Qfinal(state):
    if(state == 's0'):
        canvas.itemconfig(s0_label,fill = 'red')
        canvas.itemconfig(state0,outline = 'red')
    elif(state == 's1'):
        canvas.itemconfig(s1_label,fill = 'red')
        canvas.itemconfig(state1,outline = 'red')
        canvas.itemconfig(accept_s1,outline = 'red')
    elif(state == 's2'):
        canvas.itemconfig(s2_label,fill = 'red')
        canvas.itemconfig(state2,outline = 'red')
        canvas.itemconfig(accept_s2,outline = 'red')
    elif(state == 's3'):
        canvas.itemconfig(s3_label,fill = 'red')
        canvas.itemconfig(state3,outline = 'red')
    elif(state == 's4'):
        canvas.itemconfig(s4_label,fill = 'red')
        canvas.itemconfig(state4,outline = 'red')

'''def clear():
    canvas.after(0,reset,1)
'''

root = Tk()


title  = Label(root , text=  "DFA for langauge that must start and end with the same symbol\nL = {{0,1}* | start and end with same symbol}\nTest your String below")
title.grid(row = 0)
entryString = Entry(root )
entryString.grid(row = 1 , column  = 0)
button = Button(root, text = "Submit",command=getString)
button.grid(row = 2 ,column =0)
#reset = Button(root,text = 'reset' ,command =clear)
#rese
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
