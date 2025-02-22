import random
import tkinter as tk
from tkinter import messagebox

def new_game():
    global word, guessed_letters, attempts
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    update_display()

def update_display():
    display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    word_label.config(text=display)
    attempts_label.config(text=f"Attempts left: {attempts}")

def guess_letter():
    global attempts
    guess = entry.get().lower()
    entry.delete(0, tk.END)
    
    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Please enter a single valid letter.")
        return
    
    if guess in guessed_letters:
        messagebox.showinfo("Already Guessed", "You already guessed that letter.")
        return
    
    guessed_letters.add(guess)
    
    if guess in word:
        if set(word).issubset(guessed_letters):
            messagebox.showinfo("Congratulations!", f"You guessed the word: {word}")
            new_game()
    else:
        attempts -= 1
        if attempts == 0:
            messagebox.showerror("Game Over", f"The word was: {word}")
            new_game()
    
    update_display()

# Initialize game
words = ["python", "developer", "hangman", "challenge", "programming"]
word = ""
guessed_letters = set()
attempts = 6

# Create UI
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x300")

word_label = tk.Label(root, text="", font=("Arial", 20))
word_label.pack(pady=20)

attempts_label = tk.Label(root, text="", font=("Arial", 14))
attempts_label.pack()

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack(pady=10)

new_game_button = tk.Button(root, text="New Game", command=new_game)
new_game_button.pack()

new_game()
root.mainloop()
