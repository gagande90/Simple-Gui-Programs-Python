import tkinter as tk                                                    

gui = tk.Tk()        
gui.title("GUI") 
gui.resizable(False, False)

gui.update()
print(gui.winfo_width())
print(gui.winfo_height())

gui.mainloop()




















