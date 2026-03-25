import random
from Wordlist import words

HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# wordList = ["orange", "watermalen", "camel"]

lives = len(HANGMAN) - 1
wrong_guess = 0

choosen_word = random.choice(words)
print(choosen_word)

print("Welcome to Hangman")
print(HANGMAN[0])

place_holder = ""
for place in range(len(choosen_word)):
    place_holder += "_"

print(place_holder)

game_over = False

correct_letter = []

while not game_over :
    guess = input("Guess a letter: ").lower()
    display = ""

    if guess not in choosen_word:
        wrong_guess += 1
        lives -= 1

        print("Wrong Guess")

        if lives == 0:
            print("You Lose")
            game_over = True

    for letter in choosen_word:
        if guess == letter:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
            
    print(display)  
    if "_" not in display:
        game_over = True
        print("You Won!")

    print(HANGMAN[wrong_guess])
