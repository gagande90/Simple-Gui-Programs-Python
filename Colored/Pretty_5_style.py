import tkinter as tk                                                    
from tkinter import ttk

gui = tk.Tk()        
gui.title("GUI") 
gui.resizable(False, False)
gui.configure(background='blue')

style = ttk.Style()
style.configure('TButton', background='orange')
 
ttk.Button(gui, text='Hi there...').grid()
ttk.Button(gui, text='Hi there...').grid(column=1)
ttk.Button(gui, text='Hi there...').grid(column=2)


gui.mainloop()




















