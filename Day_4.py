import random
random_integer = random.randint(1, 10)
random_float = random.random() * 20  # OR
random_float_2 = random.uniform(1, 10)

# random_head_tail = random.randint(0, 1)
# if random_head_tail == 0:
#     print("Head")
# else:
#     print("Tail")

# print(random_head_tail)

friends = ["ali", "bob", "talib", "raza", "zaid"]
# Option - 1
# print(random.choice(friends))
# Option - 2
random_friends = random.randint(0, len(friends) - 1)
# print(friends[random_friends])

# -----------------------------------------------

# Rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]
computer_choice = random.randint(0, 2)
user_choice = int(input("What do you choose. Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if 0 <= user_choice <= 2:
    print("You Choose\n", game_list[user_choice])

print("Computer Choose \n", game_list[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("Please choose correctly.") 
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose!")
elif user_choice == computer_choice:
    print("It's draw.")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice > user_choice:
    print("You Lose!")