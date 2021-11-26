# import tkinter as tk
# import tkinter.ttk as ttk
# import PIL
# import random

# root = tk.Tk()

# root.geometry('800x800')
# root.title("Scrabble : The boat Voyage")
# # label = ttk.Label(root, text="Score : 9999").pack()

# bg_image = tk.PhotoImage(file="meow.png")
# img = tk.PhotoImage(file="meow2.png")
# bg_image.paste(img, (0, 0), img)
# bg_image.save('NewImg.png', "PNG")

# NewImg = tk.PhotoImage(file='NewImg.png')

# tkimage = tk.PhotoImage(NewImg)

# label = tk.Label(
#     root,
#     image=tkimage,
# )
# label.place(x=0, y=0)


# root.mainloop()

from PIL import Image

import numpy as np

# Create Image
img = Image.open("meow.png")

background = Image.open("meow2.png")

background.paste(img, (0, 0), img)
background.save('NewImg.png', "PNG")

NewImg = Image.open('NewImg.png')

# Use Image
tkimage = ImageTk.PhotoImage(NewImg)

panel1 = Label(root, image=tkimage)
panel1.grid(row=0, column=2, sticky=E)
root.mainloop()  # Start the GUI
