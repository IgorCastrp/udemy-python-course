
with open("new_file.txt") as file:
    anki = file.read()

newtext = ""
for item in anki:
    if " " in item:
        item.replace(" ", "")
    newtext += item

print(newtext)
