# import Tkinter
import tkinter as tk
# import Pillow
from PIL import Image, ImageTk

# creating window
root = tk.Tk()
# add name and icon
root.title("Fox exite")
root.iconbitmap(r"photo/fox.ico")


# adding images 
img1 = ImageTk.PhotoImage(Image.open(r'photo/img1.png'))
img2 = ImageTk.PhotoImage(Image.open(r'photo/img2.jpg'))
img3 = ImageTk.PhotoImage(Image.open(r'photo/img3.jpg'))
img4 = ImageTk.PhotoImage(Image.open(r'photo/img4.png'))

image_list = [img1,img2,img3,img4]
current_index = 0


label = tk.Label(root, image=image_list[0])
label.grid(row=0, column=0, columnspan=3)


def forward():
    global current_index
    current_index = (current_index + 1) % len(image_list)
    label.config(image=image_list[current_index])

def backward():
    global current_index
    current_index = (current_index - 1) % len(image_list)
    label.config(image=image_list[current_index])


backward = tk.Button(root, text="<<", command=backward)
Quit = tk.Button(root, text="Quit progarm" , command=root.quit)
forward = tk.Button(root, text=">>", command=forward)

backward.grid(row=1,column=0)
Quit.grid(row=1,column=1)
forward.grid(row=1,column=2)

root.mainloop()