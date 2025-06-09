import json
import os
import random
import time

print("Welcome to the quiz!")
print("Valid answer types: 'ad', 'b', 'c', 'abcd', 'acd' etc.")

class BColors:
    CORRECT = '\033[92m'
    INCORRECT = '\033[91m'
    NORMAL = '\033[0m'
    BLUE = '\033[94m'

questions = []
jsonPath = os.path.join(os.path.dirname(__file__), '..', 'internal', 'questions.json')
with open(jsonPath, 'r', encoding='utf-8-sig') as file:
    for question in json.load(file):
        questions.append(question)

try:
    while True:
        print(BColors.BLUE + "Please let me know if a question is wrong by forking, making a pr and updating it")
        userInput = input(BColors.NORMAL + "How many questions do you want to answer? (write all if you want to answer all questions): ")
        numberOfQuestions = len(questions)
        if userInput != "all":
            userInput = int(userInput)
            if userInput < numberOfQuestions:
                numberOfQuestions = userInput

        userScore = 0
        indexesOfQuestions = [i for i in range(len(questions))]
        wrongQuestions = []

        for i in range(numberOfQuestions):
            print(BColors.NORMAL + "Question " + str(i + 1) + "/" + str(numberOfQuestions))
            indexOfQuestion = random.choice(indexesOfQuestions)
            indexesOfQuestions.remove(indexOfQuestion)
            q = questions[indexOfQuestion]
            print(BColors.NORMAL + q['question'])

            if q['answers'] != []:
                for j in range(len(q['answers'])):
                    print(chr(j + 97) + ") " + q['answers'][j])

            userAnswer = input("Your answer: ")
            if userAnswer == q['correct']:
                print(BColors.CORRECT + "Correct!")
                userScore += 1
            else:
                print(BColors.INCORRECT + "Incorrect!")
                print("The correct answer was " + q['correct'])
                wrongQuestions.append((q, userAnswer))

        userScorePercent = userScore / numberOfQuestions * 100
        print(BColors.BLUE + "You got " + str(userScorePercent) + "%\n")

        userInput = input(BColors.NORMAL + "Do you want to review your mistakes? (y/n): ")
        if userInput == "y":
            for (q, userAnswer) in wrongQuestions:
                print(BColors.NORMAL + q['question'])
                for j in range(len(q['answers'])):
                    print(chr(j + 97) + ") " + q['answers'][j])
                print(BColors.INCORRECT + "Your answer was " + userAnswer)
                print(BColors.CORRECT + "The correct answer was " + q['correct'])

        userInput = input(BColors.NORMAL + "Do you want to play again? (y/n): ")
        if userInput == "n":
            print("Thank you for playing!")
            time.sleep(3)
            break
        else:
            print("Starting again...")
            time.sleep(2)

except KeyboardInterrupt:
    print("\n\n" + BColors.INCORRECT + "Quiz interrupted by user.")
    questionsAnswered = i if 'i' in locals() else 0
    if questionsAnswered > 0:
        userScorePercent = userScore / questionsAnswered * 100
        print(BColors.BLUE + f"You answered {questionsAnswered} questions.")
        print(BColors.BLUE + f"Your score so far: {userScorePercent:.2f}%")
    else:
        print(BColors.BLUE + "No questions were answered.")
    print(BColors.NORMAL)