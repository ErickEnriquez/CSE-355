from tkinter import * #importing library and making a reference


win = Tk() #creates an instance of our window

#theLabel = Label(win,text = "this is too easy")

#widgets  , FRAME , LABEL , BUTTON , ENTRY

label1 = Label(win,text = "username")
label2 = Label(win,text = "password")
entry1 = Entry(win)
entry2 = Entry(win)

label1.grid(row=0)
label2.grid(row=1)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=2)


win.mainloop()#runs the code