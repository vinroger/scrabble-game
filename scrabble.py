import tkinter as tk
import tkinter.ttk as ttk
import random


class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title('Scrabble : The Boat Voyage')
        self.master.geometry('600x600')

        self.root = tk.Frame(
            self, bd=3, width=800, height=800
        )
        self.root.grid(pady=(50, 0))
        self.start_game()
        self.mainloop()

    def start_game(self):
        self.answer = ""
        self.question = "PYTHON"
        self.question_list = []
        self.grade = ""
        self.button = []

        self.generate_grade()
        self.generate_undo_button()
        self.generate_buttons()
        self.generate_label()
        self.generate_restart()
        self.generate_undo_button()

    def generate_buttons(self):
        # shuffle the question, store it into arbitrary variable
        s = self.question
        lst = list(s)
        random.shuffle(lst)
        self.question_list = lst
        s = ''.join(lst)
        question = s

        # Generate the list of buttons
        for i in range(len(question)):
            self.button.append(tk.Button(
                self.root, text=question[i].upper(), command=lambda idx=i: self.assign_letter(question[idx].upper(), self.button[idx])))
            self.button[i].grid(row=1, column=i, padx=5, pady=5)
        return

    def assign_letter(self,  content, button):
        # print(self, content, button)
        self.answer = self.answer + str(content)
        self.generate_label()
        button.grid_forget()

        # print(len(self.button))
        if len(self.answer) == len(self.button):
            self.check_tf()
        return

    def generate_grade(self):
        self.grade_frame = tk.Frame(
            self.root, width=400, height=400).place()
        self.grade_label = tk.Label(self.grade_frame, text=self.grade, font=(
            'Regular script', 20), width=20)
        self.grade_label.place(x=30, y=150)

    def check_tf(self):
        if(self.answer) == self.question:
            self.grade = "Correct"
            self.generate_grade()
        else:
            self.grade = "False"
            self.generate_grade()
        return

    def generate_label(self):
        label_frame = tk.Frame(self.root, width=400, height=400).place()
        answer = tk.Label(label_frame, text=self.answer, font=(
            'Regular script', 20), width=20)
        answer.place(x=30, y=100)
        return

    def generate_restart(self):
        restart_frame = tk.Frame(self.root, width=400, height=400).place()
        restart = tk.Button(restart_frame, text="Play Again",
                            font=('Regular script', 20), width=20, command=self.restart)
        restart.place(x=30, y=200)
        return

    def restart(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.start_game()
        return

    def undo(self):
        try:
            index_of_undo = self.question_list.index(self.answer[-1])
            self.answer = self.answer[:-1]
            self.button[index_of_undo].grid(
                row=1, column=index_of_undo, padx=5, pady=5)

            # Regenerate the Correct or False
            self.grade = ""
            self.generate_grade()
            self.generate_label()
        except:
            return
        return

    def generate_undo_button(self):
        undo_frame = tk.Frame(self.root, width=400, height=400).place()
        undo = tk.Button(undo_frame, text="Undo", font=(
            'Regular script', 15), width=20, command=self.undo)
        undo.place(x=30, y=270)
        return


def main():
    Game()


if __name__ == "__main__":
    main()
