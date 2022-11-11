# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("Day26/nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter : row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter any single word:").upper()
try:
    output_data = [phonetic_dict[letter] for letter in word]
except:
    print("Sorry, only letters in the alphabet please")
else:
    print(output_data)