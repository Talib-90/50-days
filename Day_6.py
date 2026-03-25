def function_with_input(name): # name is parameter
    print(f"Hello {name}")
    print(f"How do you do {name}")

# function_with_input("Talib") # Passing value is argument

def life_in_weeks(age):
    yearsLeft = 70 - age
    weeksLeft = yearsLeft * 52
    print(f"You have {weeksLeft} weeks left.")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# greet_with("Ali", "North") # Positional argumant
# greet_with(location="New Karachi", name="Ali") # Keyword argument

# Love Calculator
# def calculate_love_score(name1, name2):
#     addNames = (name1 + name2).lower()
#     t = addNames.count("t")
#     r = addNames.count("r")
#     u = addNames.count("u")
#     e = addNames.count("e")
#     addTrue = str(t + r + u + e)

#     l = addNames.count("l")
#     o = addNames.count("o")
#     v = addNames.count("v")
#     e = addNames.count("e")
#     addLove = str(l + o + v + e)

#     result = (addTrue + addLove)
#     print(result)

# calculate_love_score("Kanye West","Kim Kardashian")