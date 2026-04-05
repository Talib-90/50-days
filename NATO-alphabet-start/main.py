import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
valueDict = {}
nato_csv = pandas.read_csv("NATO-alphabet-start/nato_phonetic_alphabet.csv")
# for index, row in nato_csv.iterrows():
#     valueDict[row.letter] = row.code

# OR
phonetic_data = {row.letter: row.code for index, row in nato_csv.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
result = [phonetic_data[letter] for letter in user_input]
print(result)