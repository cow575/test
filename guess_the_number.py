import random

def guess_the_number():
    number_to_guess = random.randint(1, 10)
    attempts = 0
    max_attempts = 3

    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between 1 and 10. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts!")
                return
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print(f"\nSorry, you ran out of attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
