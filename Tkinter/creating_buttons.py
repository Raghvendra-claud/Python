# import Tkinter
import tkinter as tk

# creating window
root = tk.Tk()

def myclick():
    mylabel = tk.Label(root, text="Hey looked I'm clicked")
    mylabel.pack()

button = tk.Button(root,text="Click me!", command=myclick, fg="blue", background="red")

''' other parametres:
    change size of button use: padx = ,pady = 
    state="disabled" for disable button
'''
button.pack()

root.mainloop()