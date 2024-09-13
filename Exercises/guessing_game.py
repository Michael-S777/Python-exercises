# Python exercise
# Guessing game
import random

def guessing_game():
    """Generate a random integer from 1 to 100.
    
    Ask the user repeatedly to guess the number.
    Until they guess correctly, tell them to guess higher or lower.
    """
    while True:
        answer = random.randint(1, 100)  # Range from 1 to 100
        print("I'm thinking of a number between 1 and 100.")
        
        while True:
            try:
                user_guess = int(input('What is your guess? '))
                if user_guess < 1 or user_guess > 100:
                    print("Please guess a number between 1 and 100.")
                    continue
            except ValueError:
                print("Please enter a valid integer.")
                continue

            if user_guess == answer:
                print(f'Right! The answer is {user_guess}.')
                break

            if user_guess < answer:
                print(f'Your guess of {user_guess} is too low!')

            else:
                print(f'Your guess of {user_guess} is too high!')

        play_again = input("Do you want to play again? (yes/no) ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    guessing_game()
