name_list = []
with open("../17-Mail-Merge/Input/Names/invited_names.txt") as names:
    for name in names:
        name_list.append(name.strip())

letter_list = []
with open("../17-Mail-Merge/Input/Letters/starting_letter.txt") as letters:
    for letter in letters:
        letter_list.append(letter.strip())
        for i in letter_list:
            if i == "":
                letter_list.remove(i)


last_name = "[name]"
for name in name_list:

    changed_string = letter_list[0].replace(f"{last_name}", name)
    letter_list[0] = changed_string

    with open(f"../17-Mail-Merge/Output/ReadyToSend/letter_for_{name}.txt", "w") as card:
        for i in letter_list:
            card.write(str(i))
            card.write("\n\n")

    last_name = name