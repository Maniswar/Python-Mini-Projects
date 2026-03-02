import random

EASY_LEVEL_ATTEMPTS     = 10
MEDIUM_LEVEL_ATTEMPTS   = 7
HARD_LEVEL_ATTEMPTS     = 5
def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == 'medium':
        return MEDIUM_LEVEL_ATTEMPTS
    elif level_chosen == 'hard':
        return HARD_LEVEL_ATTEMPTS
    
def Check_answer(Guessed_Number, answer, attempts):
    if Guessed_Number < answer:
        print("Your Guess is too low!!")
        return attempts-1
    elif Guessed_Number > answer:
        print("Your Guess is too 'high'!!!")
        return attempts-1
    else:
        print(f"Hurray Your Guess is right and the answer was {Guessed_Number}")
def game():
    print("Let me think of a number between 1 to 50.")
    answer = random.randint(1,50)
    print(answer)
    level = input("Choose level of difficulty...Type 'easy' or 'medium' or 'hard': ").lower()
    attempts = set_difficulty(level)
    if attempts != EASY_LEVEL_ATTEMPTS and attempts !=MEDIUM_LEVEL_ATTEMPTS and attempts !=HARD_LEVEL_ATTEMPTS:
        print("You Have Entered A Wrong Value Kindly Please Check Again")
        return
    Guessed_Number = 0 
    while Guessed_Number != answer:
        print(f"You have {attempts} attempts remaining to guess the number!")
        Guessed_Number = int(input("Guess a Number: "))
        attempts = Check_answer(Guessed_Number, answer, attempts)
        if attempts == 0:
          print("You are out of Guesses... You lose!")
          print(f"The answer was {Guessed_Number}")
          return
        elif Guessed_Number != answer:
            print("Guess again!")

game()