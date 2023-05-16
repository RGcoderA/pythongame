import random


def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2


def check_answer(num1, num2, answer):
    correct_answer = num1 + num2
    return answer == correct_answer


def play_game():
    score = 0
    num_questions = 5

    for _ in range(num_questions):
        num1, num2 = generate_question()
        question = f"What is {num1} + {num2}? "
        user_answer = int(input(question))

        if check_answer(num1, num2, user_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print(f"\nGame over! You scored {score} out of {num_questions}.")


play_game()
