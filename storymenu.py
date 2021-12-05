# import module needed
import gameclass as gameclass
import tkinter as tk

import game_over as gameover

# write the new window function which
# will be called when button pressed

font_used = "Consolas"
padding = 30
intro_general = "Good day Young Adventurer!\n I'm Frank the Cat!\n Let us embark on an adventure together to explore some new terrains.\n There will be 3 adventures,\n you will be given 5 lives and 5 hints for each adventure\n and all you need to do is unscramble the words!\n But beware, if you mispell a word,\n you will lose a life, and that puts us in danger!\nSo, give it your all and \nlet's go have some fun!"
intro_easy = "Good day Young Adventurer!\n I'm Frank the Cat!\n I got myself into deep trouble\n and I need YOUR help to cross the rough seas.\nYou will be given 5 lives and 5 hints. \nAll you need to do is unscramble the words!\n But beware, if you mispell a word, you will lose a life,\n and that puts us in danger!\nSo, give it your all and let's cross the river together!"
intro_med = "Phew!\n  Thanks to you, we made it pass those dangerous waters!\n  Unfortunately, I need your help again to \n drive through this treacherous terrain!\n This time, its not going to be as easy as before. \n But I know you can do it!"
intro_hard = "Whoo!\n  That was tough,\n  but we made it once again!\n  You are unstoppable!\n  My last challenge for you is to help me \n fly through these turbulent and stormy skies. \n Are you up for it?\n I know you are!\n Let's embark on this last adventure together!"


class StoryMenu(tk.Tk):
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
        self.intro = ""

        f = open('level.txt', 'r')
        a = f.read()
        f.close()
        a = int(a)

        if a == 0:
            self.intro = intro_easy
            self.image_intro = "img/frame/boat_0_0.png"
        elif a == 1:
            self.intro = intro_med
            self.image_intro = "img/frame/truck_0_0.png"
        elif a == 2:
            self.intro = intro_hard
            self.image_intro = "img/frame/boat_0_0.png"
        else:
            # change a first
            f = open('level.txt', 'r')
            a = f.read()
            level_now = 0
            f.close()

            f = open('level.txt', 'w')
            f.write(str(level_now))
            f.close()
            self.return_to_main_menu()
            return

        self.answer_label = tk.Label(self, text=self.intro, background="white", font=(
            font_used, 15))
        self.answer_label.pack(pady=padding)

        # creating the meow picture

        bg_image2 = tk.PhotoImage(file=self.image_intro)
        label2 = tk.Label(
            self,
            image=bg_image2,
        )
        label2.pack(pady=10)

        button = tk.Button(self, text="Continue", font=(
            font_used, 30),
            command=lambda: self.init_game())
        button.pack(pady=10)

        button = tk.Button(self, text="Quit", font=(
            font_used, 20),
            command=lambda: self.destroy())
        button.pack()
        self.mainloop()

    def return_to_main_menu(self):
        self.destroy()
        gameover.GameOver()

    def init_game(self):
        self.destroy()
        gameclass.Game()
