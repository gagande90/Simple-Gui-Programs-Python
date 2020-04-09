import tkinter as tk                            
from tkinter import ttk                         

gui = tk.Tk()        
gui.title("Our GUI Title")                           

frame = ttk.LabelFrame(gui, text="A frame surrounding widgets")
frame.pack(padx=10, pady=5)               

entry_list = []
label_list = []

def button_callback(idx):
    label_list[idx].config(foreground='green')
    text1.insert(tk.END, entry_list[idx].get() + '\n')
    if idx == 0:
        progress_bar.start()
        text2.insert(tk.END, '  starting Progressbar...\n')
        label_list[idx].config(text='Running...')
    elif idx ==1:
        progress_bar.stop()
        text2.insert(tk.END, '  stopping Progressbar...\n')
        label_list[idx].config(text='Stopped...')


button_names = [
    'Start Progress',
    'Stop Progress',
    'Button 2',
    'Button 3']

for idx in range(4):
    lbl_var = "label" + str(idx)
    lbl_var = ttk.Label(frame, text="Hello Label " + str(idx))
    lbl_var.grid(row=idx, column=0)
    label_list.append(lbl_var)
        
    ttk.Button(frame, text=button_names[idx], command= lambda cur_idx=idx: button_callback(cur_idx)).\
                grid(row=idx, column=1) 
    
    entry_var = "entry" + str(idx)
    entry_var = tk.Entry(frame, textvariable=tk.StringVar(value="   <default entry> " + str(idx)))
    entry_var.grid(row=idx, column=2)  
    entry_list.append(entry_var)


for child in frame.winfo_children():                
    child.grid_configure(padx=8, pady=3)          


frame_2 = ttk.LabelFrame(gui, text="Another frame")
frame_2.pack(padx=10, pady=5)   

paned = tk.PanedWindow(frame_2, sashwidth=4, relief='solid', 
                       orient='vertical')
paned.pack()

text1 = tk.Text(paned, height=8, width=40)
paned.add(text1)       

text2 = tk.Text(paned, height=8, width=40)
paned.add(text2) 

gui.update()
gui_width = gui.winfo_width()
progress_bar = ttk.Progressbar(gui, length=gui_width, mode='determinate')          
progress_bar.pack()


gui.mainloop()                                  





























