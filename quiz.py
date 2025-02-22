def run_quiz():
    # Expanded list of Duck Dynasty questions
    quiz = [
        {
            "question": "What is the name of the family business featured in Duck Dynasty?",
            "options": ["A. Duck Commander", "B. Duck Hunters Inc.", "C. Beard Bros", "D. Cajun Calls"],
            "answer": "A"
        },
        {
            "question": "Which Robertson family member is known for his wild stories and iced tea obsession?",
            "options": ["A. Phil", "B. Willie", "C. Si", "D. Jase"],
            "answer": "C"
        },
        {
            "question": "In what state does the Robertson family live?",
            "options": ["A. Texas", "B. Louisiana", "C. Alabama", "D. Mississippi"],
            "answer": "B"
        },
        {
            "question": "What ZZ Top song is used as the theme for Duck Dynasty?",
            "options": ["A. La Grange", "B. Sharp Dressed Man", "C. Gimme All Your Lovin'", "D. Legs"],
            "answer": "B"
        },
        {
            "question": "What did Phil Robertson invent that started the Duck Commander empire?",
            "options": ["A. Camouflage Pants", "B. Duck Call", "C. Beard Trimmer", "D. Fishing Lure"],
            "answer": "B"
        },
        {
            "question": "Which brother is the CEO of Duck Commander?",
            "options": ["A. Jase", "B. Jep", "C. Willie", "D. Alan"],
            "answer": "C"
        },
        {
            "question": "What does Uncle Si call almost everyone he meets?",
            "options": ["A. Buddy", "B. Jack", "C. Partner", "D. Hoss"],
            "answer": "B"
        },
        {
            "question": "What sport did Phil Robertson play in college before turning down an NFL career?",
            "options": ["A. Baseball", "B. Football", "C. Basketball", "D. Wrestling"],
            "answer": "B"
        },
        {
            "question": "What unusual item did Si win in a raffle at the donut shop?",
            "options": ["A. A Lawnmower", "B. A Camper", "C. A Duck Boat", "D. A Giant Duck Call"],
            "answer": "B"
        },
        {
            "question": "Which family member released a cookbook called 'Miss Kay’s Duck Commander Kitchen'?",
            "options": ["A. Korie", "B. Missy", "C. Kay", "D. Sadie"],
            "answer": "C"
        },
        {
            "question": "What did Willie accidentally hit Korie with while training for a family football game?",
            "options": ["A. A Football", "B. A Duck Call", "C. A Lawn Chair", "D. A Fishing Rod"],
            "answer": "A"
        },
        {
            "question": "What did the Duck Commander employees build to celebrate the company’s 40th anniversary?",
            "options": ["A. World’s Largest Duck Call", "B. A Giant Beard Statue", "C. A Duck Blind", "D. A Camo Truck"],
            "answer": "A"
        },
        {
            "question": "Which country did Willie take the family to after landing a client for duck calls?",
            "options": ["A. Canada", "B. Scotland", "C. Australia", "D. Ireland"],
            "answer": "B"
        },
        {
            "question": "What does the show typically end with the family doing?",
            "options": ["A. Hunting Ducks", "B. Praying Around the Table", "C. Singing a Song", "D. Telling Jokes"],
            "answer": "B"
        }
    ]

    score = 0
    total_questions = len(quiz)

    print("Welcome to the Ultimate Duck Dynasty Quiz!")
    print("Answer each question by typing the letter (A, B, C, or D). Get ready to prove you’re a true fan, Jack!\n")

    # Loop through each question
    for i, q in enumerate(quiz, 1):
        print(f"Question {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        user_answer = input("Your answer: ").strip().upper()

        # Check if the answer is correct
        if user_answer == q["answer"]:
            print("Correct! You’re happier than a tornado in a trailer park!")
            score += 1
        else:
            print(f"Nope! The right answer was {q['answer']}. Better luck next time, Jack!")
        print()

    # Calculate percentage and display results
    percentage = (score / total_questions) * 100
    print(f"Quiz complete! You scored {score} out of {total_questions} — that’s {percentage}%!")

    # Viral result messages
    if percentage == 100:
        result = "Perfect score! You’re the Duck Commander of trivia! Share this on X and challenge your buddies, Jack!"
    elif percentage >= 80:
        result = "Hot dang! You’re a Robertson-level expert! Post this score on X and see who can top it!"
    elif percentage >= 50:
        result = "Not bad, partner! You know your duck calls from your squirrel brains. Share this on X to flex a little!"
    else:
        result = "Looks like you’re stuck in the duck blind! Rewatch some episodes and try again. Share this on X for a redemption arc!"
    
    print(result)
    print("Tag your friends and see if they’ve got what it takes to beat you!")

# Run the quiz
if __name__ == "__main__":
    run_quiz()