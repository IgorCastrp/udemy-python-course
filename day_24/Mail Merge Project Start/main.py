PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_files:
    names = names_files.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

















################## MY CODE ###################

# with open("Input/Names/invited_names.txt", mode="r") as file:
#     list_names = file.readlines()
#     print(list_names)
#
#
# with open("Input/Letters/starting_letter.txt", mode="r") as file:
#     std = file.read()
#
#
# for name in list_names:
#     new_name = name.strip("\n")
#     new_std = std.replace("[name]", new_name)
#     print(new_std)
#     with open(f"Output/testt/letter_for_{new_name}.txt", mode="w") as file:
#         file.write(new_std)


# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
    
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
