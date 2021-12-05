# import module needed
import gameclass as gameclass
import tkinter as tk
import mainmenu as mainmenu
# write the new window function which
# will be called when button pressed

font_used = "Consolas"
padding = 30
congrats = "\nThanks for playing our game!"
devs = "Scrabble Developers:\n\nChai Gien Lyn\nCheong Hao Shaun\nGizelle Lim\nRK Suriya Varshan\nVincentius Roger K"


class GameOver(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Frank's Scrabble Game")
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

        self.answer_label = tk.Label(self, text=congrats, background="white", font=(
            font_used, 30))
        self.answer_label.pack(pady=30)

        self.answer_label = tk.Label(self, text=devs, background="white", font=(
            font_used, 20))
        self.answer_label.pack(pady=padding)

        quit_button = tk.Button(self, text="Quit", font=(
            font_used, 20),
            command=self.destroying)
        quit_button.pack(pady=padding)

    def destroying(self):
        self.destroy()
