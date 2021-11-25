import tkinter as tk
import tkinter.ttk as ttk
import random

root = tk.Tk()

root.geometry('800x800')
root.title("Scrabble : The boat Voyage")
# label = ttk.Label(root, text="Score : 9999").pack()

background_image = tk.PhotoImage("/img/meow.png")

background_label = tk.Label(
    root, image=background_image, text="hiii", font=("Times New Roman", 72))
background_label.pack()
background_label.image = background_image

root.mainloop()
