import tkinter as tk                                                    

gui = tk.Tk()        
gui.title("GUI") 
gui.resizable(False, False)
gui.geometry("200x200") 

label = tk.Label(gui, text='Hi there...')
label.pack()

gui.update()
print(gui.winfo_width())
print(gui.winfo_height())

gui.mainloop()




















