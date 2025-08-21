import random # Import the random module, allowing us to use a random number generation function

# Display the rules of the game
def display_rules():
    print("\nRules: \n")
    print("1. I will think of a number between 1 and 100.")
    print("2. You have to guess the number.")
    print("3. I will tell you if your guess is too high, too low, or correct.")

def display_difficulty_options():
    print("\nThere are 3 different difficulties; Easy, Medium & Hard.")
    print("\nThe difficulty will affect the number of attempts you receive to guess the number.")
    print("Easy will give you 10 attempts.")
    print("Medium will give you 7 attempts.")
    print("Hard will give you 5 attempts.")
    print("\nBefore we get started, choose your difficulty!")

def generate_number():
    return random.randint(1, 100)
    
number_to_guess = generate_number()

def easy_game():
    number_to_guess = generate_number()
    attempts = 1

    print("\nLevel: Easy")
    print("\nI have thought of a number between 1 and 100. Try to guess it in 10 attempts!")
    while True:
        try:
            player_guess = int(input("Enter your guess: "))
            break
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 100.")

    while player_guess != number_to_guess and attempts < 10:
        if player_guess < number_to_guess:
            print("Your guess is too low! Try again.")
        else:
            print("Your guess is too high! Try again.")
        while True:
            try:
                player_guess = int(input("Enter your guess: "))
                break
            except ValueError:
                print("Invalid input! Please enter an integer between 1 and 100.")
        attempts += 1

    if player_guess == number_to_guess:
        print(f"\nCongratulations! You've guessed the number correctly in {attempts} attempts!")
    else:
        print(f"\nSorry, you've used all your attempts. The number was {number_to_guess}.")
    play_again()

def medium_game():
    number_to_guess = generate_number()
    attempts = 1

    print("\nLevel: Medium")
    print("\nI have thought of a number between 1 and 100. Try to guess it in 7 attempts!")
    while True:
        try:
            player_guess = int(input("Enter your guess: "))
            break
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 100.")

    while player_guess != number_to_guess and attempts < 7:
        if player_guess < number_to_guess:
            print("Your guess is too low! Try again.")
        else:
            print("Your guess is too high! Try again.")
        while True:
            try:
                player_guess = int(input("Enter your guess: "))
                break
            except ValueError:
                print("Invalid input! Please enter an integer between 1 and 100.")
        attempts += 1

    if player_guess == number_to_guess:
        print(f"\nCongratulations! You've guessed the number correctly in {attempts} attempts!")
    else:
        print(f"\nSorry, you've used all your attempts. The number was {number_to_guess}.")
    play_again()

def hard_game():
    number_to_guess = generate_number()
    attempts = 1

    print("\nLevel: Hard")
    print("\nI have thought of a number between 1 and 100. Try to guess it in 5 attempts!")
    while True:
        try:
            player_guess = int(input("Enter your guess: "))
            break
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 100.")

    while player_guess != number_to_guess and attempts < 5:
        if player_guess < number_to_guess:
            print("Your guess is too low! Try again.")
        else:
            print("Your guess is too high! Try again.")
        while True:
            try:
                player_guess = int(input("Enter your guess: "))
                break
            except ValueError:
                print("Invalid input! Please enter an integer between 1 and 100.")
        attempts += 1

    if player_guess == number_to_guess:
        print(f"\nCongratulations! You've guessed the number correctly in {attempts} attempts!")
    else:
        print(f"\nSorry, you've used all your attempts. The number was {number_to_guess}.")
    play_again()

# Function to handle ending the game
def end_game():
    print("\nGame Over!")
    print("Thank you for playing!")

# Function to handle playing again
def play_again():
    while True:
        response = input("\nDo you want to play again? (Yes/No): ")
        if response.lower() in ['yes', 'y']:
            main()
            break
        elif response.lower() in ['no', 'n']:
            end_game()
            break
        else:
            print("Invalid input! Please enter 'Yes' or 'No'.")

def main():
    print("Welcome to Harangad's Number Guessing Game!")
    display_rules()
    display_difficulty_options()
    while True:
        difficulty = input("Enter Easy, Medium or Hard: ").strip().lower()
        if difficulty == "easy":
            easy_game()
            break
        elif difficulty == "medium":
            medium_game()
            break
        elif difficulty == "hard":
            hard_game()
            break
        else:
            print("Invalid input! Please enter 'Easy', 'Medium', or 'Hard'.")

main()