with open("Day_16/myFile.txt") as file:
    content = file.read()
    print(content)

# If file does't exist create it using write or edit 
# with open("Day_16/newFile.txt", "w") as data:
#     data.write("New File Created.")

# Append or add text in the file
with open("Day_16/newFile.txt", "a") as data:
    data.write("\nLine added.")

file.close()