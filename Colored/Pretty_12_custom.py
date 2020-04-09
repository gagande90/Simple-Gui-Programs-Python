import tkinter as tk                                                    
from tkinter import ttk

gui = tk.Tk()        
gui.title('GUI') 

img_regular = tk.PhotoImage(file='Solid_Blue.gif') 
img_focus = tk.PhotoImage(file='Blue_Curved_small.gif') 

style = ttk.Style()

style.element_create('custom_element', 'image', img_regular, ('focus', img_focus), border=15) 

style.layout('custom_element', [('custom_element', {'sticky': 'NSWE'})])

frame = ttk.Frame(style='custom_element', padding=10)
frame.pack(fill='x')

frame1 = ttk.Frame(style='custom_element', padding=10)
frame1.pack(fill='x')

entry = ttk.Entry(frame, width=40)
entry.pack(fill='x')
entry.bind('<FocusIn>', lambda _: frame.state(['focus']))
entry.bind('<FocusOut>', lambda _: frame.state(['!focus']))

entry1 = ttk.Entry(frame1)
entry1.pack(fill='x')
entry1.bind('<FocusIn>', lambda _: frame1.state(['focus']))
entry1.bind('<FocusOut>', lambda _: frame1.state(['!focus']))

gui.mainloop()




















