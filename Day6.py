import random

def math_quiz():
    score = 0
    total_questions = 5

    print("➗ Welcome to the Math Quiz Game!")
    print(f"Answer {total_questions} random math questions.\n")

    for q in range(1, total_questions + 1):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])

        if operation == '+':
            correct_answer = num1 + num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2

        print(f"Question {q}: What is {num1} {operation} {num2}?")
        try:
            user_answer = int(input("👉 Your answer: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        if user_answer == correct_answer:
            score += 1
            print("✅ Correct!\n")
        else:
            print(f"❌ Wrong! The correct answer was {correct_answer}.\n")

    print("🏁 Quiz Over!")
    print(f"🎯 Your Score: {score}/{total_questions}")

    if score == total_questions:
        print("🌟 Perfect! You are a math genius!")
    elif score >= total_questions // 2:
        print("👍 Well done! Keep improving!")
    else:
        print("😅 Practice makes perfect!")

if __name__ == "__main__":
    math_quiz()
