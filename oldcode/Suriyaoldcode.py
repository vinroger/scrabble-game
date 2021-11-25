from tkinter import*
import random as ran
game = Tk()
game.title("Scrambble")
game.geometry("800x600")
list_of_words = [["PYTHON", "MEOW", "FRANK", "HAOSH", "GIZELLE", "LYN"], ["A programming language", "Cat Sound",
                    "u know it", "multi-talented", "poker face", "hard working"]]
no_of_words = list(range(0,len(list_of_words[0])-1))

#scrambled word text properties 
scrambled_text_properties = Label(game, text="", font=("Consolas", 48))
scrambled_text_properties.pack(pady=20, padx=00)

#shuffler
def mix_words():
    global word_no
    global word
    word_no = (ran.choice(no_of_words))
    word= list_of_words[0][word_no]

    break_word = list(word)
    ran.shuffle(break_word)
    #print(break_word)
    mixed=''
    for i in break_word:
        mixed = mixed+i + " "
    scrambled_text_properties.config(text=mixed)

def check_answer():
    if word == (ans.get()).upper():
        ans_text_properties.config(text="You are Right!")
    else:
        ans_text_properties.config(text="oops! You are wrong")

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

hint_text_properties = Label(game, text="", font=("Consolas", 18))
hint_text_properties.pack(pady=20, padx=00)

ans_text_properties = Label(game, text="", font=("Consolas", 18))
ans_text_properties.pack(pady=20, padx=00)

mix_words()
game.mainloop()

