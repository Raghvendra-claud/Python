# import Tkinter
import tkinter as tk

# creating window
root = tk.Tk()

# creating a label widget (output into the screen)
mylabel = tk.Label(root, text='Hello World!')

# shoving into the screen
mylabel.pack()

root.mainloop()