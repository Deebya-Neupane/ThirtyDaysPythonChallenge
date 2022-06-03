# Quiz Game.

def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Country")
guess1 = input("Which country owns Mt.Everest? ")
check_guess(guess1, "Nepal")
guess2 = input("Which country has the most islands in the world? ")
check_guess(guess2, "Sweden")
guess3 = input("By size, what is the largest country in the world? ")
check_guess(guess3, "Russia")
print("Your Score is "+ str(score))

