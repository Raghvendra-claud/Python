# import Tkinter
import tkinter as tk

# creating window
root = tk.Tk()

# creating a label widget (output into the screen)
mylabel = tk.Label(root, text='Hello World!')
mylabel1 = tk.Label(root, text='Hello I\'m John Elder')

# shoving into the screen(using grid)
mylabel.grid(row=0,column=0)
mylabel1.grid(row=1,column=1)

root.mainloop()