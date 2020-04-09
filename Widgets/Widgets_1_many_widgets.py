import tkinter as tk                            
from tkinter import ttk                         

gui = tk.Tk()        
gui.title("Our GUI Title")                           

frame = ttk.LabelFrame(gui, text="A frame surrounding widgets")
frame.pack(padx=10, pady=5)               

entry_list = []
def button_callback(idx):
    entry_list[idx].config(textvariable=tk.StringVar(value='  Button {} was clicked!'.\
                                                     format(idx)))

for idx in range(4):
    ttk.Label(frame, text="Hello Label " + str(idx)).\
                grid(row=idx, column=0)
        
    ttk.Button(frame, text="Click Me " + str(idx), command= lambda cur_idx=idx: button_callback(cur_idx)).\
                grid(row=idx, column=1) 
    
    entry_var = "entry" + str(idx)
    entry_var = tk.Entry(frame, textvariable=tk.StringVar(value="   <default entry> " + str(idx)))
    entry_var.grid(row=idx, column=2)  
    entry_list.append(entry_var)


for child in frame.winfo_children():                
    child.grid_configure(padx=8, pady=3)          
      
gui.mainloop()      

                            





























