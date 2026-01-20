# import Tkinter
import tkinter as tk
# import Pillow
# from PIL import Image, ImageTk

# creating window
root = tk.Tk()
# add name and icon
root.title("Fox exite")
root.iconbitmap("fox.ico")

# adding images 
my_img = tk.PhotoImage(file="img1.png")
label = tk.Label(root, image=my_img)
label.pack()


# quit button
button = tk.Button(root, text="Quit progarm" , command=root.quit)
button.pack()

root.mainloop()