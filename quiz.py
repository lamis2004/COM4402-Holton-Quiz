"""Console-based multiple-choice quiz for the Holton College Digital Quiz System (PoC)."""

# QUESTIONS is a list of dictionaries. Each dictionary contains:
#   - "text":    the question text
#   - "options": a list of four possible answers
#   - "answer":  the correct option number (1-4)

QUESTIONS = [
    {
        "text": "Which operator checks equality in Python?",
        "options": ["=", "==", "===", "!="],
        "answer": 2,
    },
    {
        "text": "What does range(1, 6) generate in a Python for-loop?",
        "options": [
            "1, 2, 3, 4, 5, 6",
            "0, 1, 2, 3, 4, 5",
            "1, 2, 3, 4, 5",
            "2, 3, 4, 5, 6",
        ],
        "answer": 3,
    },
    {
        "text": "What is the purpose of break inside a loop?",
        "options": [
            "Skip the current iteration and continue",
            "End the loop immediately",
            "Restart the loop from the beginning",
            "Pause the program",
        ],
        "answer": 2,
    },
    {
        "text": "Which of the following is a valid f-string in Python?",
        "options": [
            'print(f"Score: {score}")',
            'print("Score: {score}")',
            'print(f"Score: score")',
            'print("fScore: " + {score})',
        ],
        "answer": 1,
    },
    {
        "text": "Which line correctly appends the value 5 to the end of a list called nums?",
        "options": [
            "nums.add(5)",
            "nums.append(5)",
            "nums.insert_end(5)",
            "append(nums, 5)",
        ],
        "answer": 2,
    },
    {
        "text": "Which is the correct way to start a while loop in Python?",
        "options": [
            "while (x > 0) then:",
            "while x > 0:",
            "while x > 0 do:",
            "while x > 0 {",
        ],
        "answer": 2,
    },
]


def check_answer(user_answer_str, correct_answer):
    """
    Validate the user's answer and check if it is correct.

    Args:
        user_answer_str (str): The raw input entered by the user.
        correct_answer (int): The correct option number (1–4).

    Returns:
        tuple[bool, bool]:
            valid_input (bool): True if the input is numeric (0–9).
            is_correct (bool): True if the answer matches correct_answer.
    """
    if not user_answer_str.isdigit():
        # Non-numeric input – handled as invalid
        print("Invalid input.")
        return False, False

    user_answer = int(user_answer_str)

    if user_answer == correct_answer:
        print("Correct!")
        return True, True

    # Numeric but not equal to the correct answer (including 0 or 5)
    print("Incorrect.")
    return True, False


def run_quiz():
    """Run the quiz once and display the final score."""
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

        valid_input, is_correct = check_answer(user_answer, question["answer"])

        # Increase score only when the input is valid and the answer is correct
        if valid_input and is_correct:
            score += 1

        question_number += 1

    print("\nQuiz Finished!")
    print(f"Your final score is {score} out of {len(QUESTIONS)}")
    print("Thank you for playing the Holton College Quiz!")


def main():
    """Entry point of the application."""
    print("Welcome to the Holton College Quiz!")
    print("Please answer by typing 1, 2, 3, or 4 for each question.\n")
    run_quiz()


if __name__ == "__main__":
    main()
