import tkinter as tk                            
from tkinter import ttk                         

gui = tk.Tk()        
gui.title("Our GUI Title")                           

frame = ttk.LabelFrame(gui, text="A frame surrounding widgets")     # gui is parent of frame
frame.pack(padx=10, pady=5)

ttk.Label(frame, text="Hello Label").\
            grid(row=0, column=0)                                   # frame is parent           

ttk.Button(frame, text="Click Me!").\
            grid(row=0, column=1)               

tk.Entry(frame, textvariable=tk.StringVar(value="     <default entry>")).\
            grid(row=0, column=2)               

for child in frame.winfo_children():                
    child.grid_configure(padx=10, pady=10)          
      
gui.mainloop()                                  





























