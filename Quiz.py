import random
from datetime import datetime

# =====================================
# QUIZ QUESTIONS
# =====================================

questions = [

    {
        "question": "Who is Shah Rukh Khan?",
        "options": [
            "WWE Wrestler",
            "Plumber",
            "Actor",
            "Astronaut"
        ],
        "answer": 3
    },

    {
        "question": "What is the capital of France?",
        "options": [
            "Berlin",
            "Paris",
            "Rome",
            "London"
        ],
        "answer": 2
    },

    {
        "question": "Which planet is known as the Red Planet?",
        "options": [
            "Earth",
            "Venus",
            "Mars",
            "Jupiter"
        ],
        "answer": 3
    }
]

# =====================================
# ADMIN PANEL
# =====================================

def admin_panel():

    print("\n========== ADMIN PANEL ==========")

    while True:

        add_question = input(
            "\nDo you want to add a question? (y/n): "
        ).lower()

        if add_question == "n":
            break

        elif add_question == "y":

            question_text = input(
                "\nEnter question: "
            )

            option1 = input("Option 1: ")
            option2 = input("Option 2: ")
            option3 = input("Option 3: ")
            option4 = input("Option 4: ")

            while True:

                try:

                    correct_answer = int(
                        input(
                            "Correct option number (1-4): "
                        )
                    )

                    if correct_answer not in [1, 2, 3, 4]:
                        print("Enter between 1-4")
                        continue

                    break

                except ValueError:
                    print("Invalid input!")

            # Add question

            questions.append({

                "question": question_text,

                "options": [
                    option1,
                    option2,
                    option3,
                    option4
                ],

                "answer": correct_answer
            })

            print("Question added successfully!")

        else:
            print("Invalid input!")


# =====================================
# MAIN MENU
# =====================================

print("===================================")
print("        QUIZ GAME")
print("===================================")

while True:

    print("\n1. Play Quiz")
    print("2. Admin Panel")
    print("3. Exit")

    choice = input("\nEnter choice: ")

    # =================================
    # PLAY QUIZ
    # =================================

    if choice == "1":

        # Shuffle questions

        random.shuffle(questions)

        player_name = input(
            "\nEnter your name: "
        )

        correct_answers = 0
        total_money = 0

        print("\n========== QUIZ START ==========")

        # =============================
        # QUIZ LOOP
        # =============================

        for i, question in enumerate(questions):

            print(f"\nQuestion {i + 1}")
            print(question["question"])

            options = question["options"]

            print(f"1. {options[0]}")
            print(f"2. {options[1]}")
            print(f"3. {options[2]}")
            print(f"4. {options[3]}")

            # =========================
            # INPUT VALIDATION
            # =========================

            while True:

                try:

                    answer = int(
                        input(
                            "\nEnter answer (1-4): "
                        )
                    )

                    if answer not in [1, 2, 3, 4]:
                        print(
                            "Please enter between 1-4"
                        )
                        continue

                    break

                except ValueError:
                    print("Invalid input!")

            # =========================
            # CHECK ANSWER
            # =========================

            if answer == question["answer"]:

                print("Correct Answer!")

                correct_answers += 1

                # ₹1000 per correct answer

                total_money += 1000

                print(
                    f"You won ₹1000"
                )

            else:

                correct_option = (
                    options[
                        question["answer"] - 1
                    ]
                )

                print("\nWrong Answer!")
                print(
                    f"Correct Answer: "
                    f"{correct_option}"
                )

                break

        # =============================
        # FINAL RESULT
        # =============================

        print("\n========== RESULT ==========")

        print(
            f"Player Name: {player_name}"
        )

        print(
            f"Correct Answers: "
            f"{correct_answers}"
        )

        print(
            f"Total Money Won: "
            f"₹{total_money}"
        )

        # =============================
        # SAVE RESULT
        # =============================

        current_date = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        
        # save score in file
        
        with open("quiz_scores.txt","a") as file:
            file.write(
                f"Date: {current_date} | "
                f"Player: {player_name} | "
                f"Correct Answers: "
                f"{correct_answers} | "
                f"Money Won: "
                f"{total_money}\n"
            )

        print(
            "\nResult saved successfully!"
        )

    # =================================
    # ADMIN PANEL
    # =================================

    elif choice == "2":

        admin_panel()

    # =================================
    # EXIT
    # =================================

    elif choice == "3":

        print("\nThanks for playing!")
        break

    else:
        print("Invalid choice!")
