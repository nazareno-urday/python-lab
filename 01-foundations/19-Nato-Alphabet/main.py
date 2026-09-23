import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter:row.code for (index,row) in df.iterrows()}
print(alphabet)

name = (input("Enter your name: ").upper())
phonetic_name = [alphabet[letter] for letter in name]
print(phonetic_name)