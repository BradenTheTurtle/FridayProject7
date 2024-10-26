import random  # Import the random module to generate a random number

# Greeting message
print("Welcome to the Number Guessing Game!")
play = input("Do you want to play? (yes/no): ").strip().lower()

# If the user wants to play
if play == "yes":
    # Generate a secret number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # Initialize a variable to track if the user has guessed correctly
    guessed_correctly = False

    # Loop until the user guesses the correct number
    while not guessed_correctly:
        guess = int(input("Guess a number between 1 and 10: "))  # Prompt for a guess

        # Check the guess against the secret number
        if guess < secret_number:
            print("Too low! Try again.")  # Hint if the guess is too low
        elif guess > secret_number:
            print("Too high! Try again.")  # Hint if the guess is too high
        else:
            print("Congratulations! You've guessed the number!")  # Correct guess
            guessed_correctly = True  # Exit the loop once guessed correctly

# If the user does not want to play
else:
    print("Maybe next time!")

# Farewell message
print("Thank you for playing! Goodbye!")
