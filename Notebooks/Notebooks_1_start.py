import tkinter as tk                            
from tkinter import ttk                         

gui = tk.Tk()        
gui.title("GUI")


tabs_frame = ttk.Frame(gui)
tabs_frame.grid(row=0, column=0, sticky='W')

display_area = ttk.Labelframe(gui, text=' Tab Display Area ')
display_area.grid(row=1, column=0, sticky='WE')

note1 = ttk.Notebook(tabs_frame)
note1.grid(row=0, column=0)

note2 = ttk.Notebook(tabs_frame)
note2.grid(row=1, column=0)

# create and add tabs to Notebooks
for tab_no in range(5):
    tab1 = ttk.Frame(note1)                                 # Create a tab for notebook 1
    tab2 = ttk.Frame(note2)                                 # Create a tab for notebook 2
    note1.add(tab1, text=' Tab {} '.format(tab_no + 1))     # Add tab notebook 1
    note2.add(tab2, text=' Tab {} '.format(tab_no + 1))     # Add tab notebook 2


gui.mainloop() 
























