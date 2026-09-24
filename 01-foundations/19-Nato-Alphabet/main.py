import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index,row) in df.iterrows()}

def generate_phonetic():
    name = (input("Enter your name: ").upper())
    try:
        phonetic_name = [alphabet[letter] for letter in name]

    except KeyError:
        print("Sorry, your name is invalid.")
        generate_phonetic()

    else:
        print(phonetic_name)

generate_phonetic()