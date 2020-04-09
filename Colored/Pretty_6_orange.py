import tkinter as tk                                                    
from tkinter import ttk

gui = tk.Tk()        
gui.title("GUI") 
gui.resizable(False, False)
gui.configure(background='blue')

tk.Button(gui, text='Hi there...', bg='orange', relief='flat', width=9).grid()
tk.Button(gui, text='Hi there...', bg='orange', relief='flat', width=9).grid(column=1)
tk.Button(gui, text='Hi there...', bg='orange', relief='flat', width=9).grid(column=2)


gui.mainloop()




















