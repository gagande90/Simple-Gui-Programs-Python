import tkinter as tk                                                    

gui = tk.Tk()        
gui.title("GUI") 
gui.resizable(False, False)

label = tk.Label(gui, text='Hi there...', padx=100, pady=10)
label.pack()

gui.update()
print(gui.winfo_width())
print(gui.winfo_height())

gui.mainloop()




















