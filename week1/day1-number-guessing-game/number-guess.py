import tkinter as tk # Import the tkinter module, allowing us to create a GUI for the game.
import random # Import the random module, allowing us to use a random number generation function.

# Global variables
number_to_guess = 0  # This will hold the number that the player has to guess
attempts_left = 0  # This will hold the number of attempts the player has left
max_attempts = 0  # This will hold the maximum number of attempts allowed

def start_game(max_attempts):
    global number_to_guess, attempts_left
    number_to_guess = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts_left = max_attempts

    difficulty_frame.pack_forget()  # Hide the difficulty selection frame
    game_frame.pack()
    result_label = tk.Label(result_frame, text=f"I have chosen a number between 1 and 100.\nYou have {attempts_left} attempts!")
    result_label.pack()

def check_guess():
    global attempts_left
    user_guess = int(entry.get())  # Get the user's guess from the entry widget
    entry.delete(0, tk.END)  # Clear the entry widget for the next guess

    while attempts_left > 0:
        if user_guess == number_to_guess:
            result_label = tk.Label(result_frame, text=f"🎉 Correct! The number was {number_to_guess}.")
        else:
            if user_guess < number_to_guess:
                result_label = tk.Label(result_frame, text="📉 Too low!")
            else:
                result_label = tk.Label(result_frame, text="📈 Too high!")

    attempts_left -= 1

    if attempts_left == 0:
        result_label = tk.Label(result_frame, text=f"💔 Game over! The number was {number_to_guess}.")
    result_label.pack()

def disable_game():
    submit_btn.config(state=tk.DISABLED)
    play_again_btn.pack()

def reset_game():
    entry.delete(0, tk.END)
    submit_btn.config(state=tk.NORMAL)
    play_again_btn.pack_forget()
    game_frame.pack_forget()
    difficulty_frame.pack()

# GUI Setup

window = tk.Tk()  # Create the main window
window.title("Harangad's Number Guessing Game")  # Set the title of the window
window.geometry("1200x800")  # Set the size of the window

welcome_frame = tk.Frame(window)  # Create a frame for the welcome message
welcome_frame.pack()

welcome_label = tk.Label(welcome_frame, text="Welcome to Harangad's Number Guessing Game!")
welcome_label.pack()

rules_frame = tk.Frame(window)  # Create a frame for rules
rules_frame.pack()

rules_label = tk.Label(rules_frame, text="Rules: \n1. I will think of a number between 1 and 100.\n2. You have to guess the number.\n3. I will tell you if your guess is too high, too low, or correct.")
rules_label.pack()

difficulty_options_frame = tk.Frame(window)
difficulty_options_frame.pack()

difficulty_options_label = tk.Label(difficulty_options_frame, text="\nThere are 3 different difficulties; Easy, Medium & Hard.\nThe difficulty will affect the number of attempts you receive to guess the number.\nEasy will give you 10 attempts.\nMedium will give you 7 attempts.\nHard will give you 5 attempts.")
difficulty_options_label.pack()

difficulty_frame = tk.Frame(window)  # Create a frame for difficulty options
difficulty_frame.pack()

difficulty_label = tk.Label(difficulty_frame, text="Before we get started, choose your difficulty!")
difficulty_label.pack()

tk.Button(difficulty_frame, text="Easy", command=lambda: start_game(10)).pack(side=tk.LEFT, padx=5, pady=5)  # Easy difficulty
tk.Button(difficulty_frame, text="Medium", command=lambda: start_game(7)).pack(side=tk.LEFT, padx=5, pady=5)  # Medium difficulty
tk.Button(difficulty_frame, text="Hard", command=lambda: start_game(5)).pack(side=tk.LEFT, padx=5, pady=5)  # Hard difficulty

game_frame = tk.Frame(window) # Create a frame for the game
game_frame.pack()

entry = tk.Entry(game_frame)
entry.pack(pady=10)

submit_btn = tk.Button(game_frame, text="Submit Guess", command=check_guess)
submit_btn.pack(pady=5)

result_frame = tk.Frame(window)  # Create a frame for the result
result_frame.pack()

play_again_btn = tk.Button(game_frame, text="Play Again", command=reset_game)
play_again_btn.pack(pady=5)

window.mainloop()