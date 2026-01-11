QUESTIONS = [
    {
        "text": "Which operator checks equality in Python?",
        "options": ["=", "==", "===", "!="],
        "answer": 2
    },
    {
        "text": "What does range(1, 6) generate in a Python for-loop?",
        "options": [
            "1, 2, 3, 4, 5, 6",
            "0, 1, 2, 3, 4, 5",
            "1, 2, 3, 4, 5",
            "2, 3, 4, 5, 6"
        ],
        "answer": 3
    },
    {
        "text": "What is the purpose of break inside a loop?",
        "options": [
            "Skip the current iteration and continue",
            "End the loop immediately",
            "Restart the loop from the beginning",
            "Pause the program"
        ],
        "answer": 2
    },
    {
        "text": "Which of the following is a valid f-string in Python?",
        "options": [
            'print(f"Score: {score}")',
            'print("Score: {score}")',
            'print(f"Score: score")',
            'print("fScore: " + {score})'
        ],
        "answer": 1
    },
    {
        "text": "Which line correctly appends the value 5 to the end of a list called nums?",
        "options": [
            "nums.add(5)",
            "nums.append(5)",
            "nums.insert_end(5)",
            "append(nums, 5)"
        ],
        "answer": 2
    },
    {
        "text": "Which is the correct way to start a while loop in Python?",
        "options": [
            "while (x > 0) then:",
            "while x > 0:",
            "while x > 0 do:",
            "while x > 0 {"
        ],
        "answer": 2
    }
]


def run_quiz():
    score = 0
    question_number = 1

    for question in QUESTIONS:
        print("\nQuestion", question_number)
        print(question["text"])

        option_number = 1
        for option in question["options"]:
            print(f"{option_number}. {option}")
            option_number += 1

        user_answer = input("Enter your answer (1-4): ")

        if user_answer.isdigit():
            if int(user_answer) == question["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        else:
            print("Invalid input.")

        question_number += 1

    print("\nQuiz Finished!")
    print(f"Your final score is {score} out of {len(QUESTIONS)}")


def main():
    print("Welcome to the Holton College Quiz")
    run_quiz()


if __name__ == "__main__":
    main()
