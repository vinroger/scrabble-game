
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

root.geometry('400x400')
root.title("Scrabble : The boat Voyage")
# label = ttk.Label(root, text="Score : 9999").pack()
frame = ttk.Frame(root)
frame.pack()

global s


def hi(event):
    print("hello world")


global Score
Score = 0
global Meow
Meow = " meow"


def add_counter(event):
    global Score
    Score += 1
    global Meow
    Meow += " meow"
    if (len(Meow) % 20 >= 0 and len(Meow) % 20 <= 6):
        Meow += "\n"
    str_score.set('Meow Counter:' + str(Score))
    str_meow.set(str(Meow))


str_score = tk.StringVar()
score_label = tk.Label(root, textvariable=str_score, font=(
    'Regular script', 20), width=15, height=1)
str_score.set('Meow Counter:' + str(Score))
score_label.place(x=30, y=30)

str_meow = tk.StringVar()
meow_label = tk.Label(root, textvariable=str_meow, font=(
    'Regular script', 15), width=20)
str_meow.set(str(Meow))
meow_label.place(x=30, y=100)


button = ttk.Button(root, text="meow")
button.place(x=120, y=70)

button.bind('<Button-1>', add_counter)


# def meow():
#     s = ''
#     for i in range(counter):
#         s += "meow "
#     return s


# w = tk.Label(root, text=meow)
# w.pack()

root.mainloop()
