from tkinter import *
import tkinter.ttk as ttk
import random as ran
game = Tk()
game.title("Scrambble")
game.geometry("800x600")
list_of_words = [["PYTHON", "MEOW", "FRANK", "HAOSH", "GIZELLE", "LYN"], ["A programming language", "Cat Sound",
                    "u know it", "multi-talented", "poker face", "hard working"]]
no_of_words = list(range(0,len(list_of_words[0])-1))



#VARIABLES TO TRY
lost_value = -100
win_value = 100

#lifeline
lifeline = ["❤","❤","❤","❤","❤"]

lifeline_label_properties = Label(game, text="Lifeline", font=("Consolas", 15, "bold"),fg="red")
lifeline_label_properties.pack(padx=35,side=TOP, anchor=NE)
lifeline_label_properties = Label(game, text="", font=("default",15, "bold"),fg="red")
lifeline_label_properties.pack(side=TOP, anchor=NE, padx =10)


#theme for progress bar
ttk_style = ttk.Style()
ttk_style.theme_use('classic')
ttk_style.configure("red.Horizontal.TProgressbar", foreground='red', background='red')

#Progress Bar
progress_bar_properties = ttk.Progressbar(game, style="", orient=HORIZONTAL, length=300, mode='determinate')
progress_bar_properties.pack(pady=(30, 0))

#Progress
progress = 0
progress_text = Label(game, text="Progress: " + str(progress) +" %", font=("Consolas", 15))
progress_text.pack(pady=(0,20))







#scrambled word text properties 
scrambled_text_properties = Label(game, text="", font=("Consolas", 48))
scrambled_text_properties.pack(pady=20)

#shuffler
def mix_words():
    hint_text_properties.config(text="")
    ans.delete(0, END)
    ans_text_properties.config(text="")
    global word_no
    global word
    word_no = (ran.choice(no_of_words))
    word= list_of_words[0][word_no]

    break_word = list(word)
    ran.shuffle(break_word)
    #print(break_word)
    mixed=break_word[0]
    for i in range(1, len(break_word)):
        mixed = mixed+" " + break_word[i]
    scrambled_text_properties.config(text=mixed)

def check_answer():
    global progress
    if word == (ans.get()).upper():
        ans_text_properties.config(text="You are Right!")

        #progress update
        progress+=10
        progress_bar_properties["value"] = abs(progress)
        progress_text.config(text="Progress: " +str(progress)+" %")
        check_progress()
        lifeline_check()
        mix_words()
    else:
        ans_text_properties.config(text="oops! You are wrong")
        try:
            lifeline.pop()
        except:
            pass

        #progress update
        # progress-=20
        # progress_bar_properties["value"] = abs(progress)
        # progress_text.config(text="Progress: " +str(progress) +" %")
        lifeline_check()
        

def check_progress():
    global progress

    if progress >= win_value:
        game_over_win()

def lifeline_check():

    lifeline_text = ""
    for i in lifeline:
        lifeline_text += i + " "
    lifeline_label_properties.config(text= lifeline_text)

    if len(lifeline) == 0:
        game_over_lost()
    


def game_over_lost():
    for widget in game.winfo_children():
        widget.pack_forget()
    lose_text_properties = Label(game, text="): Game Over :(", font=("Consolas", 40))
    lose_text_properties.pack(pady=200)

def game_over_win():
    for widget in game.winfo_children():
        widget.pack_forget()
    lose_text_properties = Label(game, text="WOOHOOOO\n!!CONGRATSS!!\n:D", font=("Consolas", 40))
    lose_text_properties.pack(pady=200)

def generate_restart():
    ans_button = Button(button_frame, text="Play Again", command=check_answer)
    ans_button.grid(row=0, column=0, padx=10)
    game.bind('<Return>', lambda event: check_answer())
    
    
    
    

def hint():
    hint_text_properties.config(text=list_of_words[1][word_no])



ans = Entry(game, text="", font=("Consolas", 12) )
ans.pack(pady=20)

button_frame = Frame(game)
button_frame.pack(pady=30)

next_button = Button(button_frame, text="Next word", command=mix_words)
next_button.grid(row=0, column=2, padx=10)

hint_button = Button(button_frame, text="Hint", command=hint)
hint_button.grid(row=0, column=1, padx=10)

ans_button = Button(button_frame, text="Submit", command=check_answer)
ans_button.grid(row=0, column=0, padx=10)
game.bind('<Return>', lambda event: check_answer())

hint_text_properties = Label(game, text="", font=("Consolas", 18))
hint_text_properties.pack(pady=20, padx=00)

ans_text_properties = Label(game, text="", font=("Consolas", 18))
ans_text_properties.pack(pady=20, padx=00)

lifeline_check()
mix_words()
game.mainloop()

