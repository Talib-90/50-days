# # Subscripting
# print("Hello"[4])
# street_name = "Tariq Road"
# print(street_name[4] + street_name[7])
# # Concatenation
# print("122" + "223") 

# Integer = Whole Numbers
# print(111 + 998)

# # Large Numbers (_)
# print(123_456_789)

# # Float = Floating Point Numbers
# print(3.14159)

# Boolean
# print(True)
# print(False)

# print("\n ---Type---")
# print(type("Hello"))
# print(type(123))
# print(type(True))
# print(type(122.32))

# print("\n---Run without erros---")
# print("Number of letters in your name: " + str(len(input("Enter your name"))))

# Name = input("Enter your name")
# Length = len(Name)
# print(type(Name)) # Return <str>
# print(type(Length)) # Return <int>

# print("--- PEMDAS ---")
# print(" (), Exponents, *, /, +, -")
# print(2 + 8)
# print(22 - 8)
# print(2 * 8)
# print(12 / 5)
# print(12 // 5)
# print(2 ** 5)

# print(f"Answer :{3 * (3 + 3) // 3 - 3}")

# print("--- BMI Calculation ---")
# height = 1.8
# weight = 66

# bmi = weight / height ** 2
# print(round(bmi))

print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# split_bill = int(input("How many people to split the bill?"))

# total = (bill + (tip / 100) * bill) / split_bill
# print(f"Each person should pay: ${round(total, 2)}")

bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like give? 10, 12, 15" ))
split_bill = int(input("How many peoples to split the bill? "))

total = (bill + ((tip / 100) * bill)) / split_bill
print(f"Each person should pay {total}")