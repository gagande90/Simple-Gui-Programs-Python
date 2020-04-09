import tkinter as tk                            
from tkinter import ttk     
from tkinter.messagebox import showinfo                    

# Callbacks & functions
#------------------------------------------
def clear_display_area():
    for widget in display_area.grid_slaves():
        if int(widget.grid_info()["row"]) == 0:
            widget.grid_forget()  
            
            
def display_button(active_notebook, tab_no):
    btn = ttk.Button(display_area, text=active_notebook +' - Tab '+ tab_no,
                     command= lambda: showinfo("Tab Display", "Tab: " + tab_no))
    btn.grid(column=0, row=0, padx=8, pady=8)     


def notebook_callback(event):
    clear_display_area()
    
    current_notebook = str(event.widget)
    tab_no = str(event.widget.index("current") + 1)   
    
    if current_notebook.endswith('notebook'):
        active_notebook = 'Notebook 1'
    elif current_notebook.endswith('notebook2'):
        active_notebook = 'Notebook 2'
    else:
        active_notebook = ''
    
    display_button(active_notebook, tab_no)
    
    
# GUI Creation
#------------------------------------------
gui = tk.Tk()        
gui.title("GUI")


tabs_frame = ttk.Frame(gui)
tabs_frame.grid(row=0, column=0, sticky='W')

display_area = ttk.Labelframe(gui, text=' Tab Display Area ')
display_area.grid(row=1, column=0, sticky='WE', padx=5, pady=5)

display_area_label = tk.Label(display_area, text="", height=2)
display_area_label.grid(column=0, row=0)

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

# bind click-events to Notebooks       
note1.bind("<ButtonRelease-1>", notebook_callback)
note2.bind("<ButtonRelease-1>", notebook_callback)


gui.mainloop() 
























