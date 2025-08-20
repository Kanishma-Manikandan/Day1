import random

def rock_paper_scissors_best_of_3():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    winning_score = 3

    print("🎮 Welcome to Rock-Paper-Scissors (Best of 3)!")
    print("First to 3 points wins. Type 'q' anytime to quit.\n")

    while user_score < winning_score and computer_score < winning_score:
        user_choice = input("👉 Choose rock, paper, or scissors: ").lower()

        if user_choice == 'q':
            print("👋 Game exited. Thanks for playing!")
            return

        if user_choice not in options:
            print("⚠️ Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = random.choice(options)
        print(f"🖥️ Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("😐 It's a tie!\n")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            user_score += 1
            print(f"🎉 You win this round! (You: {user_score} | Computer: {computer_score})\n")
        else:
            computer_score += 1
            print(f"💻 Computer wins this round! (You: {user_score} | Computer: {computer_score})\n")

    # Game result
    if user_score == winning_score:
        print("🏆 Congratulations! You are the champion!")
    else:
        print("🤖 Computer is the champion. Better luck next time!")

if __name__ == "__main__":
    rock_paper_scissors_best_of_3()
