# Handle exception
# try:
# except:
# else:
# finally:
# File not found error
# try:
#     file = open("a_file.txt")
#     dictionary = {"Key": "value"}
#     print(dictionary["Key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Hello World!")
# except IOError:
#     print("File not writable")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist.")
# else:
#     print(file.read())
# finally:
#     raise TypeError("The error I made up")

height = float(input("Height:"))
weight = int(input("Weight:"))

if height > 3:
    raise ValueError("Height should not over 3 meters.")

bmi = weight / (height ** 2)
print(bmi)