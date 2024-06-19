import random

secret_number = random.randint(0, 5)
attempts_left = 3

print("Welcome to Number Guessing Game!")
print("You have 3 attempts to guess the secret one digit number between 0 and 5.")

while attempts_left > 0:
    print(f"Attempts left: {attempts_left}")
    guess = int(input("Enter your guess (between 0 and 5): "))
    
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Incorrect guess. Try again.")
    
    attempts_left -= 1

print(f"\nGame over! The secret number was {secret_number}.")
