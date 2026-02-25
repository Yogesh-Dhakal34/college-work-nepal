import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Set the number of guesses allowed
    max_guesses = 10
    
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_guesses} guesses to find the number.")
    
    # Main game loop
    for i in range(max_guesses):
        # Get the user's guess
        guess = int(input("What's your guess? "))
        
        # Check the guess
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {i+1} tries.")
            return
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")
    
    # If the user runs out of guesses
    print(f"Sorry, you didn't guess the number. The number was {secret_number}.")

# Start the game
guess_the_number()
