# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm?"))

# if height >= 120:
#     print("You can ride the rollercoster.")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# print(10 % 3)

# ------------------------------------

# check = int(input("Enter Number: "))
# if check % 2 == 1:
#     print("Odd")
# else:
#     print("Even")

# ------------------------------------

# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm?"))

# if height >= 120:
#     print("You can ride the rollercoster.")
#     age = int(input("What's your age?"))
#     if age <=12:
#         print("Please pay 5$.")
#     elif age <= 18:
#         print("Please pay 7$.")
#     else:
#         print("Please pay 12$.")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# ------------------------------------

# weight = 66
# height = 1.7

# bmi = weight / height ** 2
# print(bmi)
# if bmi >= 25:
#     print("overweight")
# elif bmi >= 18.5:
#     print("Normal weight")
# else:
#     print("underweight")

# ------------------------------------

# print("Welcome to the rollercoster!")
# height = int(input("What is your height in cm?"))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoster.")
#     age = int(input("What's your age?"))
#     if 45 <= age <= 55:
#         print("Enjoy free ride")
#     elif age <=12:
#         bill = 5
#         print("Child ticket 5$.")
#     elif age <= 18:
#         bill = 7
#         print("Youth ticket 7$.")
#     else:
#         bill = 12
#         print("Adult price 12$.")

#     want_photo = input("If you want a photo type y for Yes or n for No.")
#     if want_photo == 'y':
#         bill += 3
    
#     print(f"Your total bill is: {bill}")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# ------------------------------------

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# pepperoni = input("Do you want pepperoni on your pizza? (Y or N) ")
# extra_cheese = input("Do you want extra cheese? (Y or N) ")

# price = 0

# if size == "S":
#     price = 15
# elif size == "M":
#     price = 20
# elif size == "L":
#     price = 25
# else:
#     print("Please select right pizza.")

# if pepperoni == "Y":
#     price += 2
# else:
#     price += 1

# if extra_cheese == "Y":
#     price += 1

# total = print(f"Your final bill is ${price}")

# ------------------------------------

print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
road = input("You're at a cross road. Where do you want to go? \n Type \"Left\" or \"right\" ").lower()
if road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_swim = input(" Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")
    if wait_swim == "wait":
        print("You arrive at the island unharmed. There is a house with three doors.")
        color = input("\tOne red, one blue, and one yellow. Which one you choose?")
        if color == "red" or color == "blue":
            print("It's a room full of fire. Game Over!")
        elif color == "yellow":
            print("Congratulations you find a correct one. Hurry You win!")
    elif wait_swim == "swim":
        print("Game Over!")
    else:
        print("Please typed correctly.")
elif road == "right":
    print("You fell into a hole. Game Over.")
else:
    print("Please type correctly!")