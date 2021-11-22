import tkinter as tk
import tkinter.ttk as ttk
import random


list_question = ["PYTHON", "MEOW", "FRANK", "HAOSH", "GIZELLE", "LYN"]
list_description = ["A programming language", "Cat Sound",
                    "u know it", "multi-talented", "poker face", "hard working"]

font_used = "Consolas"
pad_config = "pady=20"


class Game(tk.Tk):
    def __init__(self):

        tk.Tk.__init__(self)
        self.title('Scrabble : The Boat Voyage')
        self.geometry('600x600')
        self.progress = 0
        self.start_game()
        self.mainloop()

    def start_game(self):
        randomInt = random.randint(0, len(list_question)-1)
        self.answer = " "
        self.question = list_question[randomInt]
        self.description = list_description[randomInt]
        self.question_list = []
        self.grade = " "
        self.button = []
        self.graded_boolean = False

        self.generate_progress()
        self.generate_buttons()
        self.generate_grade()
        self.generate_undo_button()
        self.generate_label()
        self.generate_restart()
        self.generate_description()
        self.generate_next()

    def generate_buttons(self):
        # shuffle the question, store it into arbitrary variable
        s = self.question
        lst = list(s)
        random.shuffle(lst)
        self.question_list = lst
        s = ''.join(lst)
        question = s

        # Generate the list of buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=30)
        for i in range(len(question)):
            self.button.append(tk.Button(
                button_frame, text=question[i].upper(), command=lambda idx=i: self.assign_letter(question[idx].upper(), self.button[idx])))
            self.button[i].grid(row=1, column=i, padx=5, pady=5)
        return

    def assign_letter(self,  content, button):
        self.answer = self.answer + str(content)
        self.delete_label()
        self.generate_label()
        button.grid_forget()

        if len(self.answer) == len(self.button):
            self.check_tf()
        return

    def generate_grade(self):

        self.grade_label = tk.Label(self, text=self.grade, font=(
            font_used, 20), width=20)
        self.grade_label.pack(pady=10)

    def check_tf(self):
        if(self.answer) == self.question:
            self.grade = "Correct"
            self.graded_boolean = True
            self.generate_grade()
        else:
            self.grade = "False"
            self.graded_boolean = True
            self.generate_grade()
        return

    def generate_label(self):

        self.answer_label = tk.Label(self, text=self.answer, font=(
            font_used, 20), width=20)
        self.answer_label.pack(pady=10)
        return

    def delete_label(self):
        self.answer_label.destroy()

    def generate_restart(self):
        restart_frame = tk.Frame(self, width=400, height=400).place()
        restart = tk.Button(restart_frame, text="Restart Progress",
                            font=(font_used, 10), width=20, command=self.restart)
        restart.place(x=30, y=470)
        return

    def restart(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.progress = 0
        self.start_game()
        return

    def undo(self):
        try:
            if(self.graded_boolean == False):
                index_of_undo = self.question_list.index(self.answer[-1])
                self.answer = self.answer[:-1]
                self.button[index_of_undo].grid(
                    row=1, column=index_of_undo, padx=5, pady=5)

                # Regenerate the Correct or False
                self.grade = ""
                self.generate_grade()
                self.delete_label()
                self.generate_label()
        except:
            return
        return

    def generate_undo_button(self):

        undo = tk.Button(self, text="Undo", font=(
            font_used, 15), width=20, command=self.undo)
        undo.pack(pady=10)
        return

    def generate_description(self):

        answer = tk.Label(self, text="Description : " + self.description, font=(
            font_used, 20), width=100, anchor="w")
        answer.pack(pady=10)
        return

    def generate_next_button(self):

        answer = tk.Label(self, text="Description : " + self.description, font=(
            font_used, 20), width=20)
        answer.pack(pady=10)
        return

    def generate_progress(self):

        self.progress_label = tk.Label(self, text="Progress: " + str(self.progress)+" %", font=(
            font_used, 20), width=20)
        self.progress_label.pack(pady=10)
        return

    def generate_next(self):

        undo = tk.Button(self, text="Next", font=(
            font_used, 15), width=20, command=self.next)
        undo.pack(pady=10)
        return

    def next(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        if(self.grade == "Correct"):
            self.progress += 20
            if(self.progress >= 100):
                self.congrats()
        else:
            self.progress -= 10
            if(self.progress < 0):
                self.game_over()
        self.start_game()

        return

    def game_over(self):

        for widget in self.winfo_children():

            widget.pack_forget()

        answer = tk.Label(self, text="GAME OVER !\nThe boat sunk and u die :(", font=(
            font_used, 20), width=100, anchor="w")
        answer.pack(pady=10)
        self.generate_restart()
        return

    def congrats(self):

        for widget in self.winfo_children():

            widget.pack_forget()

        answer = tk.Label(self, text="Congratulations!\nThe boat went across safely!", font=(
            font_used, 20), width=100, anchor="w")
        answer.pack(pady=10)
        self.generate_restart()
        return


def main():
    Game()


if __name__ == "__main__":
    main()
