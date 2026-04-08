import random

# def is_prime(number):
#     if number == 2:
#         return True
#     if number == 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True

# print(is_prime(9))        

# Number Guessing Game
numberGuessingGame = """
 _______               ___.                    ________                            .__                   ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
"""
print(numberGuessingGame)

EASY_LEVEL = 10
HARD_LEVEL = 5


def check_answer(u_number, c_number, turns):
    if u_number > c_number:
        print("Too high.")
        return turns - 1
    elif u_number < c_number:
        print("Too Loo.")
        return turns - 1
    else:
        print(f"You got it! The answer was {c_number}.")


def set_difficulty():
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choice == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def playGame():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    turns = set_difficulty()
    answer = random.randint(1, 100)
    guess = 0
    while guess != answer:
        print(f"you have {turns} attempts remaining. ")

        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You have run out of guesses, you lose. The answer is {answer}")
            return
        else:
            print("Guess again.")


playGame()
