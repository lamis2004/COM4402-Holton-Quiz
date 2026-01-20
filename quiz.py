"""Console-based multiple-choice quiz for the Holton College Digital Quiz System (PoC)."""

# QUESTIONS is a list of dictionaries. Each dictionary contains:
#   - "topic":   the topic of the question (e.g. Operators, Loops)
#   - "text":    the question text
#   - "options": a list of four possible answers
#   - "answer":  the correct option number (1-4)

QUESTIONS = [
    {
        "topic": "Operators",
        "text": "Which operator checks equality in Python?",
        "options": ["=", "==", "===", "!="],
        "answer": 2,
    },
    {
        "topic": "Loops",
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
        "topic": "Loops",
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
        "topic": "Strings and f-strings",
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
        "topic": "Lists",
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
        "topic": "Loops",
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


def get_available_topics():
    """Return a sorted list of distinct topics in the QUESTIONS list."""
    topics = {question["topic"] for question in QUESTIONS}
    return sorted(topics)


def choose_topic():
    """Allow the user to choose a topic or all topics for the quiz."""
    topics = get_available_topics()

    print("Please choose a quiz topic:")
    print("0. All topics")

    number = 1
    for topic in topics:
        print(f"{number}. {topic}")
        number += 1

    while True:
        choice = input("Enter your choice (0 for all topics): ")

        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        choice_number = int(choice)

        if choice_number == 0:
            return None  # None means all topics
        if 1 <= choice_number <= len(topics):
            return topics[choice_number - 1]

        print("Invalid choice. Please enter one of the numbers shown above.")


def get_valid_answer(num_options):
    """
    Repeatedly ask the user for an answer until a valid option number is entered.

    Returns:
        int: A valid option number between 1 and num_options (inclusive).
    """
    while True:
        user_answer = input(f"Enter your answer (1-{num_options}): ")

        if not user_answer.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        answer_number = int(user_answer)

        if 1 <= answer_number <= num_options:
            return answer_number

        print("Invalid option. Please enter one of the numbers shown above.")


def check_answer(user_answer, correct_answer):
    """
    Check if the user's answer is correct and print feedback.

    Args:
        user_answer (int): The option number chosen by the user.
        correct_answer (int): The correct option number.
    """
    if user_answer == correct_answer:
        print("Correct!")
        return True

    print("Incorrect.")
    return False


def run_quiz():
    """Run the quiz once and display the final score."""
    selected_topic = choose_topic()

    if selected_topic is None:
        questions_to_ask = QUESTIONS
        print("\nYou chose: All topics.")
    else:
        questions_to_ask = [
            question for question in QUESTIONS if question["topic"] == selected_topic
        ]
        print(f"\nYou chose topic: {selected_topic}.")

    if not questions_to_ask:
        print("There are no questions available for the selected topic.")
        return

    score = 0
    question_number = 1

    for question in questions_to_ask:
        print("\nQuestion", question_number)
        print(f"Topic: {question['topic']}")
        print(question["text"])

        option_number = 1
        for option in question["options"]:
            print(f"{option_number}. {option}")
            option_number += 1

        user_answer = get_valid_answer(len(question["options"]))

        if check_answer(user_answer, question["answer"]):
            score += 1

        question_number += 1

    print("\nQuiz Finished!")
    print(f"Your final score is {score} out of {len(questions_to_ask)}")
    print("Thank you for playing the Holton College Quiz!")


def main():
    """Entry point of the application."""
    print("Welcome to the Holton College Quiz!")
    print("You will answer multiple-choice questions by typing 1, 2, 3, or 4.\n")
    run_quiz()


if __name__ == "__main__":
    main()

