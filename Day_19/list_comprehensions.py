# List comprehension Syntex
# new_list = [newItem for item in list if test]


numbers = [1, 2, 3]
new_list = [item + 1 for item in numbers]
# print(new_list)

name = "Talib"
new_name = [letter for letter in name]

range_list = [n * 2 for n in range(1, 5)]

names = ["Ali", "Nawaz", "Sahil", "Moon", "Danish", "Suleman"]
new_names = [name.upper() if len(name) > 5 else name.lower() for name in names]

# Square Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
new_numbers = [num * num for num in numbers]

# Filtering Even Numbers
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)