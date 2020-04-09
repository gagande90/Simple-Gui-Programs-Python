import tkinter as tk                            
from tkinter import ttk                         

gui = tk.Tk()                                   

ttk.Label(gui, text="Hello Label").\
            grid(row=0, column=0)               

ttk.Button(gui, text="Click Me!").\
            grid(row=0, column=1)               

tk.Entry(gui, textvariable=tk.StringVar(value="     <default entry>")).\
            grid(row=0, column=2)               
            
gui.mainloop()                                  





























