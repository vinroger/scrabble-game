# import module needed
import gameclass as gameclass
import tkinter as tk
# write the new window function which
# will be called when button pressed

font_used = "Consolas"
padding = 30


class MainMenu(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Scrabble : The Boat Voyage")
        self.configure(background="white")
        self.geometry('800x800')
        self.iconbitmap('img/favicon.ico')
        # Full Screen
        self.fullScreenState = True
        try:
            self.attributes('-fullscreen', self.fullScreenState)
            self.bind("<F11>", lambda event: self.attributes(
                "-fullscreen", not self.attributes("-fullscreen")))
            self.bind("<Escape>", lambda event: self.attributes(
                "-fullscreen", False))
        except:
            pass

        self.answer_label = tk.Label(self, text="Welcome to Scrabble!", background="white", font=(
            font_used, 20), width=20)
        self.answer_label.pack(pady=padding)

        # creating the meow picture
        bg_image2 = tk.PhotoImage(file="img/meow3.png")
        label2 = tk.Label(
            self,
            image=bg_image2,
        )
        label2.pack(pady=padding)

        button = tk.Button(self, text="MEOW!", font=(
            font_used, 30),
            command=lambda: self.init_game())
        button.pack(pady=padding)

        button = tk.Button(self, text="Quit", font=(
            font_used, 20),
            command=lambda: self.destroy())
        button.pack(pady=padding)
        self.mainloop()

    def init_game(self):
        self.destroy()
        gameclass.Game()
