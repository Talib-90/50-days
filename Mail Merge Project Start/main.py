PLACEHOLDER = "[name]"

with open("Mail Merge Project Start/Input/Names/invited_names.txt") as file_names:
    names = file_names.readlines()

with open("Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letterContents = letter_file.read()
    for name in names:
        stripNames = name.strip()
        newLetterContents = letterContents.replace(PLACEHOLDER, stripNames)
        with open(f"Mail Merge Project Start/Output/Letter_for_{stripNames}.txt", "w") as complete_file:
            complete_file.write(newLetterContents)