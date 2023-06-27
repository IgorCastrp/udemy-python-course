import pandas as pd

data_nato = pd.read_csv("nato_phonetic_alphabet.csv")
nato_df = pd.DataFrame(data_nato)

letters_list = [letter for letter in nato_df.letter]
codes_list = [code for code in nato_df.code]

nato_dict = {letters_list[i]: codes_list[i] for i in range(len(letters_list))}
# print(nato_dict)

nato_list = []

user_word = input("Enter a word: ").upper()
for letter in user_word:
    for _ in nato_dict:
        if _ == letter:
            nato_list.append(nato_dict[_])

print(nato_list)


######### UDEMY CODE ###############

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
