import tkinter as tk                                                    
from tkinter import ttk

gui = tk.Tk()        
gui.title("GUI") 
gui.resizable(False, False)
gui.configure(background='blue')

style = ttk.Style()
style.configure('TButton', font=('', 12))


ttk.Button(gui, text='Hi there...').grid()
ttk.Button(gui, text='Hi there...').grid()
ttk.Button(gui, text='Hi there...').grid()

ttk.Label(gui, text='Hi there...', width=20, anchor='center').grid(row=0, column=1)
ttk.Label(gui, text='Hi there...', width=20, anchor='center').grid(row=1, column=1)
ttk.Label(gui, text='Hi there...', width=20, anchor='center').grid(row=2, column=1)

gui.mainloop()




















