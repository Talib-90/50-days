import random
student_score = [44, 76, 64, 89, 71, 34, 55, 100, 63, 88]

max_score = 0
for student in student_score:
    if student > max_score:
        max_score = student

add = 0
for number in range(1, 101):
    add += number

# --------------------------
# FizzBuzz Game

# for number in range(1, 31):
#     if number % 3 == 0 and number % 5 == 0: print("FizzBuzz")
#     elif number % 3 == 0: print("Fizz")
#     elif number % 5 == 0: print("Buzz")
#     else: print(number)

print("Welcome to password generator")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbols = ['!','@','#','$','%','^','&','*','(',')','+']

password_letters = int(input("How many letters would you like in your password? \n"))
password_numbers = int(input("How many numbers would you like? \n"))
password_symbol = int(input("How many symbols would you like? \n"))

# user_letter = random.choices(letters, k=password_letters)
# user_num = random.choices(numbers, k = password_numbers)
# user_sym = random.choices(symbols, k = password_symbol)

# print(f"Here is your password {''.join(user_letter)}{''.join(user_num)}{''.join(user_sym)}")
#   OR
password = ""
for num in range(0, password_letters):
    password += random.choice(letters)

for num in range(0, password_numbers):
    password += random.choice(numbers)

for num in range(0, password_symbol):
    password += random.choice(symbols)

con_list = list(password)
random.shuffle(con_list)
new_password = ''.join(con_list)
print("Your password is:",new_password)