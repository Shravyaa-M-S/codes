import tkinter as tk
from tkinter import messagebox

# Function to check the guess
def check_guess():
    global guess_count
    guess = int(entry.get())
    guess_count += 1
    
    if guess == secret_number:
        messagebox.showinfo("Result", "You Won!!!")
        reset_game()
    elif guess_count >= guess_limit:
        messagebox.showinfo("Result", "Sorry, wrong Answer!!!\n Try one more time")
        reset_game()
    else:
        messagebox.showinfo("Result", "Wrong guess. Try again.")

# Function to reset the game
def reset_game():
    global guess_count
    guess_count = 0
    entry.delete(0, tk.END)

# Set up the game variables
secret_number = 9
guess_count = 0
guess_limit = 3

# Set up the GUI
root = tk.Tk()
root.title("Number Guessing Game")

label = tk.Label(root, text="Enter a number to guess:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=check_guess)
button.pack()

root.mainloop()
