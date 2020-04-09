import tkinter as tk                                # alias tkinter as "tk"                 
from tkinter import ttk                             # ttk == "themed tk"

gui = tk.Tk()                                       # create Tk() instance and assign to variable

ttk.Label(gui, text="Hello Label").\
            grid(row=0, column=0)                   # create a themed tk label

ttk.Button(gui, text="Click Me!").\
            grid(row=0, column=1)                   # gui is the parent for the widgets

tk.Entry(gui).\
            grid(row=0, column=2)                   # using grid layout manager
            
gui.mainloop()                                      # start the main event loop to display our gui





























