import random # Import the random module, allowing us to use a random number generation function

print("Welcome to Harangad's Number Guessing Game!") # Display a welcome message

# Display the rules of the game
print("Rules:")
print("1. I will think of a number between 1 and 100.")
print("2. You have to guess the number.")
print("3. I will tell you if your guess is too high, too low, or correct.")
print("Let's get started!")

number_to_guess = random.randint(1, 100) # Generate a random number between 1 and 100

print("I have thought of a number between 1 and 100. Try to guess it!") # Prompt the user to start guessing
player_guess = int(input("Enter your guess: ")) # Get the player's first guess

# Loop until the player guesses the correct number
while player_guess != number_to_guess:
    if player_guess < number_to_guess: 
        print("Your guess is too low! Try again.")
    else:
        print("Your guess is too high! Try again.")

    player_guess = int(input("Enter your guess: "))

# End of game
print("Congratulations! You guessed the number correctly.")
print("Thank you for playing!")