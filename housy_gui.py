from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()

mb=  Menubutton ( top, text="condiments", relief=RAISED )
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="New Game",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="Next",
                          variable=ketchVar )

mb.pack()
top.mainloop()