import tkinter as tk
import tkinter.ttk as ttk
import random
import mainmenu as mainmenu


list_question = ["PYTHON", "MEOW", "FRANK", "HAOSH", "GIZELLE", "LYN"]
list_description = ["A programming language", "Cat Sound",
                    "u know it", "multi-talented", "poker face", "hard working"]

font_used = "Consolas"
pad_config = "pady=10"
win_value = 100


class Game(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self)
        self.title('Scrabble : The Boat Voyage')
        self.geometry('800x800')
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

        bg_image = tk.PhotoImage(file="sea.png")
        label = tk.Label(
            self,
            image=bg_image,
        )
        # self.update()
        label.pack()
        label.place(relx=0.5, y=150, anchor="c")

        bg_image2 = tk.PhotoImage(file="boat.png")
        label2 = tk.Label(
            self,
            image=bg_image2,
        )
        label2.pack()
        #label2.place(x=0, y=0)

        self.main_frame = tk.Frame(self, height=500, width=800)

        # self.main_frame.configure(background="white")
        self.progress = 0
        self.question = ""
        self.reset_all_globals()
        self.start_game()
        self.main_frame.pack(side="bottom")
        self.main_frame.pack_propagate(0)

        self.mainloop()

    def restart_everything(self):
        self.reset_all_globals()

        self.start_game()

    def clear_window(self):
        for widget in self.main_frame.winfo_children():
            widget.pack_forget()

    def start_game(self):
        self.clear_window()
        self.button_list = []
        self.question_list = []
        self.last_button_pressed = []
        self.last_index_pressed = []
        self.question = ""
        self.answer = ""
        # generate new question
        randomInteger = random.randint(0, len(list_question)-1)
        self.question = list_question[randomInteger]
        self.question_description = list_description[randomInteger]

        self.generate_elements()
        self.main_frame.pack(side="bottom")
        self.main_frame.pack_propagate(0)

    def reset_all_globals(self):
        self.last_button_pressed = []
        self.last_index_pressed = []
        self.progress = 0
        self.lifeline = ["❤", "❤", "❤", "❤", "❤"]
        self.question = ""
        self.button_list = []
        self.question_list = []
        self.answer = ""

    def undo(self):
        try:
            self.last_button_pressed[-1].grid(
                row=1, column=self.last_index_pressed[-1], padx=5, pady=5
            )
            self.last_button_pressed.pop()
            self.last_index_pressed.pop()
            self.answer = self.answer[:-1]
            self.answer_label.config(text=self.answer)
            return
        except:
            return

    def assign_letter(self, content, button, index):
        self.last_button_pressed.append(button)
        self.last_index_pressed.append(index)
        self.answer = self.answer + str(content)
        self.answer_label.config(text=self.answer)
        button.grid_forget()

        return

    def generate_buttons(self):
        s = self.question
        lst = list(s)
        random.shuffle(lst)
        self.question_list = lst
        s = ''.join(lst)
        question = s

        for i in range(len(question)):
            self.button_list.append(tk.Button(self.answer_buttons_frame, text=question[i].upper(
            ), command=lambda idx=i: self.assign_letter(question[idx].upper(), self.button_list[idx], idx)))
            self.button_list[i].grid(row=1, column=i, padx=5, pady=5)

    def update_lifeline(self):

        lifeline_text = ""
        for i in self.lifeline:
            lifeline_text += i + " "
        self.lifeline_label.config(text="Lifeline\n"+lifeline_text)

        if len(self.lifeline) <= 0:
            self.game_over_lost()

    def hint(self):
        self.hint_text.config(text=self.question_description)

    def check_progress(self):
        if self.progress >= win_value:

            self.game_over_win()
        return

    def game_over_win(self):
        self.clear_window()
        win_text_properties = tk.Label(
            self.main_frame, text="WOOHOOOO\n!!CONGRATSS!!\n:D", font=("Consolas", 40))
        win_text_properties.pack(pady=100)
        self.generate_restart_button()
        return

    def generate_restart_button(self):
        # restart_button
        self.restart_button = tk.Button(self.main_frame, text="Restart", font=(
            "Consolas", 30), command=self.return_to_main_menu)
        self.restart_button.pack(pady=10)
        return

    def return_to_main_menu(self):
        self.destroy()
        mainmenu.MainMenu()

    def game_over_lost(self):
        self.clear_window()
        lose_text_properties = tk.Label(
            self.main_frame, text="): Game Over :(", font=("Consolas", 40))
        lose_text_properties.pack(pady=100)
        self.generate_restart_button()
        return

    def check_answer(self):
        if self.answer == self.question.upper():
            self.grade.config(text="You are Right!")
            # progress update
            self.progress += 10
            self.progress_bar["value"] = abs(self.progress)
            self.progress_text.config(
                text="Progress: " + str(self.progress)+" %")
            self.check_progress()
            self.update_lifeline()
            if self.progress < win_value:
                self.start_game()
        else:
            for i in range(len(self.answer)):
                self.undo()
            self.grade.config(text="oops! You are wrong")
            try:
                self.lifeline.pop()
            except:
                pass

            self.update_lifeline()

        return

    def generate_elements(self):
        self.lifeline_label = tk.Label(
            self.main_frame, text="Lifeline\n", font=("default", 15, "bold"), fg="red")
        self.lifeline_label.pack(side=tk.TOP, anchor=tk.NE, padx=10)
        self.update_lifeline()

        # theme for progress bar
        ttk_style = ttk.Style()
        ttk_style.theme_use('classic')
        ttk_style.configure("red.Horizontal.TProgressbar",
                            foreground='red', background='red')

        # Progress Bar
        self.progress_bar = ttk.Progressbar(
            self.main_frame, style="", orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.progress_bar["value"] = abs(self.progress)
        self.progress_bar.pack()

        # Progress text and percentage
        self.progress_text = tk.Label(self.main_frame, text="Progress: " +
                                      str(self.progress) + " %", font=("Consolas", 15))
        self.progress_text.pack(pady=(0, 20))

        self.answer_buttons_frame = tk.Frame(self.main_frame)
        self.answer_buttons_frame.pack(pady=10)
        # loop through the question and generate buttons
        # scramble the question

        self.generate_buttons()

        self.answer_label = tk.Label(self.main_frame, text=self.answer, font=(
            font_used, 20), width=20)
        self.answer_label.pack(pady=10)

        # undo button for
        self.ans_button = tk.Button(
            self.main_frame, text="Submit", font=(
                font_used, 15), width=20, command=self.check_answer)
        self.ans_button.pack(pady=10)

        # button frame for submit hint next
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)

        self.next_button = tk.Button(
            self.button_frame, text="Next word", command=self.start_game)
        self.next_button.grid(row=0, column=0, padx=10)

        self.hint_button = tk.Button(
            self.button_frame, text="Hint", command=self.hint)
        self.hint_button.grid(row=0, column=1, padx=10)

        self.undo_button = tk.Button(
            self.button_frame, text="Undo", command=self.undo)
        self.undo_button.grid(row=0, column=2, padx=10)
        self.bind('<Return>', lambda event: self.check_answer())

        # hint for the question
        self.hint_text = tk.Label(
            self.main_frame, text="", font=("Consolas", 18))
        self.hint_text.pack(pady=10, padx=00)

        self.grade = tk.Label(
            self.main_frame, text="", font=("Consolas", 18))
        self.grade.pack(pady=10, padx=00)


# def main():
#     Game()


# if __name__ == "__main__":
#     main()
