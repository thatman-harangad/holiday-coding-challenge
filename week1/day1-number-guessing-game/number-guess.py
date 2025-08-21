import random # Import the random module, allowing us to use a random number generation function

# Display the rules of the game
def display_rules():
    print("\nRules: \n")
    print("1. I will think of a number between 1 and 100.")
    print("2. You have to guess the number.")
    print("3. I will tell you if your guess is too high, too low, or correct.")

def display_difficulty_options():
    print("\tThere are 3 different difficulties; Easy, Medium & Hard.")
    print("\n\tThe difficulty will affect the number of attempts you receive to guess the number.")
    print("\tEasy will give you 10 attempts.")
    print("\tMedium will give you 7 attempts.")
    print("\tHard will give you 5 attempts.")
    print("\nBefore we get started, choose your difficulty!")

def generate_number():
    return random.randint(1, 100)
    
number_to_guess = generate_number()

def easy_game():
    attempts = 1

    print("\nI have thought of a number between 1 and 100. Try to guess it in 10 attempts!") # Prompt the user to start guessing
    player_guess = int(input("Enter your guess: ")) # Get the player's first guess

    # Loop until the player guesses the correct number
    while player_guess != number_to_guess and attempts < 10:
        if player_guess < number_to_guess:
            print("Your guess is too low! Try again.")
        else:
            print("Your guess is too high! Try again.")
        player_guess = int(input("Enter your guess: "))
        attempts += 1 # Increment the number of attempts after each guess

    if attempts < 10:
        (f"\nCongratulations! You've guessed the number correctly in {attempts} attempts!") # Congratulate the player for guessing correctly
    else:
        (f"\nSorry, you've used all your attempts. The number was {number_to_guess}.")
    play_again() # Ask the player if they want to play again

def medium_game():
    attempts = 1

    print("\nI have thought of a number between 1 and 100. Try to guess it in 7 attempts!") # Prompt the user to start guessing
    player_guess = int(input("Enter your guess: ")) # Get the player's first guess

    # Loop until the player guesses the correct number
    while player_guess != number_to_guess and attempts < 7:
        if player_guess < number_to_guess:
            print("Your guess is too low! Try again.")
        else:
            print("Your guess is too high! Try again.")
        player_guess = int(input("Enter your guess: "))
        attempts += 1 # Increment the number of attempts after each guess

    if attempts < 7:
        (f"\nCongratulations! You've guessed the number correctly in {attempts} attempts!") # Congratulate the player for guessing correctly
    else:
        (f"\nSorry, you've used all your attempts. The number was {number_to_guess}.")
    play_again() # Ask the player if they want to play again

def hard_game():
    attempts = 1

    print("\nI have thought of a number between 1 and 100. Try to guess it in 5 attempts!") # Prompt the user to start guessing
    player_guess = int(input("Enter your guess: ")) # Get the player's first guess

    # Loop until the player guesses the correct number
    while player_guess != number_to_guess and attempts < 5:
        if player_guess < number_to_guess:
            print("Your guess is too low! Try again.")
        else:
            print("Your guess is too high! Try again.")
        player_guess = int(input("Enter your guess: "))
        attempts += 1 # Increment the number of attempts after each guess

    if attempts < 5:
        (f"\nCongratulations! You've guessed the number correctly in {attempts} attempts!") # Congratulate the player for guessing correctly
    else:
        (f"\nSorry, you've used all your attempts. The number was {number_to_guess}.")
    play_again() # Ask the player if they want to play again

# Function to handle ending the game
def end_game():
    print("\nGame Over!")
    print("Thank you for playing!")

# Function to handle playing again
def play_again():
    response = input("\nDo you want to play again? (Yes/No): ")
    if response.lower() == 'yes':
        main() # Restart game
    else:
        end_game()

def main():
    print("Welcome to Harangad's Number Guessing Game!") # Display a welcome message
    display_rules()
    display_difficulty_options()
    difficulty = input("Enter Easy, Medium or Hard: ").lower() # Get the player's choice of difficulty

    if difficulty == "easy":
        easy_game()
    elif difficulty == "medium":
        medium_game()
    elif difficulty == "hard":
        hard_game()
