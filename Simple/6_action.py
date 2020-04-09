import tkinter as tk                            
from tkinter import ttk                         

gui = tk.Tk()        
gui.title("Our GUI Title")                           

frame = ttk.LabelFrame(gui, text="A frame surrounding widgets")
frame.pack(padx=10, pady=5)

ttk.Label(frame, text="Hello Label").\
            grid(row=0, column=0)               
       
def button_callback():
    entry.config(textvariable=tk.StringVar(value='   Button was clicked!'))

ttk.Button(frame, text="Click Me!", command=button_callback).\
            grid(row=0, column=1)                            

entry = tk.Entry(frame, textvariable=tk.StringVar(value="     <default entry>"))
entry.grid(row=0, column=2)  

for child in frame.winfo_children():                
    child.grid_configure(padx=10, pady=10)          
      
gui.mainloop()                                  





























