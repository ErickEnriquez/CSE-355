from tkinter import * #importing library and making a reference


win = Tk() #creates an instance of our window

#theLabel = Label(win,text = "this is too easy")

#theLabel.pack()# lazy way , just packs the label


topFrame = Frame(win)
topFrame.pack(side  = TOP )
bottomFrame = Frame(win)
bottomFrame.pack(side = BOTTOM)#packs the bottom frame on the bottom


#button_1 = Button(topFrame,text = "BUTTON1" , fg ="red")
#button_2 = Button(topFrame,text = "BUTTON2" , fg ="blue")
#button_3 = Button(topFrame,text = "BUTTON3" , fg ="red")
#button_4 = Button(bottomFrame,text = "BUTTON4" , bg ="yellow")

#button_1.pack(side = "left")
#button_2.pack(side  = "right")
#button_3.pack()
#button_4.pack()
 

win.mainloop()#runs the code