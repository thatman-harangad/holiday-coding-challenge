import random # Import the random module, allowing us to use a random number generation function

# Display the rules of the game
def display_rules():
    print("\nRules: \n")
    print("1. I will think of a number between 1 and 100.")
    print("2. You have to guess the number.")
    print("3. I will tell you if your guess is too high, too low, or correct.")
    print("\nLet's get started!")

def generate_number():
    return random.randint(1, 100)
    
number_to_guess = generate_number()

def play_game():
    attempts = 1

    print("\nI have thought of a number between 1 and 100. Try to guess it!") # Prompt the user to start guessing
    player_guess = int(input("Enter your guess: ")) # Get the player's first guess

    # Loop until the player guesses the correct number
    while player_guess != number_to_guess:
        if player_guess < number_to_guess: 
            print("Your guess is too low! Try again.")
        else:
            print("Your guess is too high! Try again.")
        player_guess = int(input("Enter your guess: "))
        attempts += 1 # Increment the number of attempts after each guess

    print(f"\nCongratulations! You've guessed the number correctly in {attempts} attempts!") # Congratulate the player for guessing correctly
    play_again() # Ask the player if they want to play again

# Function to handle ending the game
def end_game():
    print("\nGame Over!")
    print("Thank you for playing!")

# Function to handle playing again
def play_again():
    response = input("\nDo you want to play again? (Yes/No): ")
    if response.lower() == 'yes':
        play_game()
    else:
        end_game()

def main():
    print("Welcome to Harangad's Number Guessing Game!") # Display a welcome message
    display_rules()
    play_game()

main()