def new_game():
    guesses = []
    correct_guesses = 0
    question_number = 1
    for i in questions:
        print(i)
        for j in answers[question_number - 1]:
            print(j)
        print()
        guess = input("Pleases select A,B,C or D: ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(i), guess)
        question_number += 1
    print(correct_guesses)
    display_score(correct_guesses,guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        print()
        return 1
    else:
        print("Wrong!")
        print()
        return 0

def display_score(correct_guesses, guesses):
    print("RESULTS")
    print("ANSWERS: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("GUESSES: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = correct_guesses / len(guesses) * 100
    print("Your score is " + str(score) + "%")

def play_again():
    response = None
    play_again = ["yes", "no"]
    while response not in play_again:
        response = input("Play again?: yes/no   ")
        response = response.lower()
    if response == "yes":
        return True
    else:
        return False

questions = {
    "Who created Python?: " : "A",
    "What year was Phyton created?: " : "B",
    "Python is tributed to which comedy group?: " : "C",
    "Is the Earth round?: " : "A"
}

answers = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
]

new_game()

while play_again():
    new_game()

print("Have a wonderful day!")