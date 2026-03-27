<<<<<<< HEAD
with open("Day_16/myFile.txt") as file:
    content = file.read()
    print(content)

# If file does't exist create it using write or edit 
# with open("Day_16/newFile.txt", "w") as data:
#     data.write("New File Created.")

# Append or add text in the file
with open("Day_16/newFile.txt", "a") as data:
    data.write("\nLine added.")
=======
# file = open("Day_16/myFile.txt")
# context = file.read()
# print(context)

with open("Day_16/myFile.txt") as file: # by default it's read only mode
    repl = file.read()
    print(repl.replace("Talib", "ali"))

# with open("Day_16/myFile.txt", "a") as file: 
#     file.write("\nNew Line added.")

#Opening a File that doesn't exit in write mode will create it 
# with open("Day_16/new_file.txt", "w") as file: 
#     file.write("New Line added.")

>>>>>>> cb04bf0 (Add new file day_16)

file.close()