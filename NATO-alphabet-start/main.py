import pandas

nato_csv = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_data = {row.letter: row.code for index, row in nato_csv.iterrows()}
while True:
    user_input = input("Enter a word: ").upper()
    try:
        result = [phonetic_data[letter] for letter in user_input]
    except KeyError:
        print("Sorry, Only letters in the alphabet please")
        continue
    else:
        print(result)
        break
