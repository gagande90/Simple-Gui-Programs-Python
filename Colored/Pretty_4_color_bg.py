import tkinter as tk                                                    
from tkinter import ttk

gui = tk.Tk()        
gui.title("GUI") 
gui.resizable(False, False)
gui.configure(background='Blue')
 
ttk.Button(gui, text='Hi there...').grid()
ttk.Button(gui, text='Hi there...').grid(column=1)
ttk.Button(gui, text='Hi there...').grid(column=2)


gui.mainloop()




















