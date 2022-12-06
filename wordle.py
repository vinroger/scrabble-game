from tkinter import messagebox
import tkinter as tk
import random


root = tk.Tk()
root.title('Wordle')
frame = tk.Frame(root)
frame.pack()
# variables
green = '#27e512'
yellow = '#e8ef0e'
gray = '#4c4c4c'
font = 'Verdana, 38'
letters = []
letter_count = 0
guess = ''
words = []
winner = False

# get the words from a file
with open('five.txt', 'r') as file:
    data = file.readlines()
    for i in data:
        words.append(i[:-1])


# key events
def key_pressed(event):
    global letter_count, guess
    if not winner:
        if event.char >= 'a' and event.char <= 'z' or event.char >= 'A' and event.char <= 'Z':
            if letter_count <= 29:
                letters[letter_count]['text'] = event.char.upper()
                letters[letter_count].focus()
                guess = guess + event.char.upper()
                letter_count += 1
                if letter_count % 5 == 0:
                    if guess.lower() in words:
                        check_word(guess)
                        guess = ''
                    else:
                        letter_count -= 5
                        go_again()
                        guess = ''
            if letter_count == 30:
                win_lose(winner)


def win_lose(winner):
    if not winner:
        title = 'You Lose'
        message = f'The word was {word}'
    else:
        title = 'You Win'
        message = 'Well done, you got it in {} guess(s)'.format(int(letter_count / 5))
    play_again = messagebox.askquestion(title=title, message=f'{message}.\nWould you like to play again?')
    if play_again == 'yes':
        layout()
    else:
        root.destroy()
        quit()


def go_again():
    for i in range(5):
        letters[letter_count + i]['text'] = ' '


# check word
def check_word(guess):
    global winner
    btn_index = letter_count - 5
    for i, letter in enumerate(guess):
        if letter == word[i]:
            letters[btn_index + i]['bg'] = green
            letters[btn_index + i]['activebackground'] = green
        elif letter in word:
            if guess.count(letter) >= 1 and guess.count(letter) == word.count(letter):
                letters[btn_index + i]['bg'] = yellow
                letters[btn_index + i]['activebackground'] = yellow
            else:
                letters[btn_index + i]['bg'] = gray
                letters[btn_index + i]['activebackground'] = gray
        else:
            letters[btn_index + i]['bg'] = gray
            letters[btn_index + i]['activebackground'] = gray
    if guess == word:
        winner = True
        win_lose(winner)


# layout
def layout():
    global frame, letter_count, winner, guess, word
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack()
    letters.clear()
    letter_count = 0
    winner = False
    guess = ''
    word = random.choice(words).upper()
    #print(word)
    for row in range(6):
        for col in range(5):
            btn = tk.Button(frame, text=' ', width=1, bg='white',
                            activebackground='white', font=font)
            btn.grid(row=row, column=col, padx=3, pady=5)
            letters.append(btn)
    menu = tk.Menu(root)
    root.config(menu=menu)
    new_game = tk.Menu(menu)
    menu.add_command(label='New Game', command=layout)
            

root.bind('<Key>', key_pressed)
layout()
root.mainloop()