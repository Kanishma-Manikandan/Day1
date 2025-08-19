import random

def number_guess_game():
    print("🎯 Welcome to the Number Guessing Game!")
    number = random.randint(1, 20)
    attempts = 0

    while True:
        guess = input("Guess a number between 1 and 20 (or 'q' to quit): ")

        if guess.lower() == 'q':
            print("👋 Exiting game. The number was:", number)
            break

        if not guess.isdigit():
            print("⚠️ Please enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("🔼 Too low, try again.")
        elif guess > number:
            print("🔽 Too high, try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} tries.")
            break

if __name__ == "__main__":
    number_guess_game()
