<h1 align="center">📡 NATO Phonetic Alphabet Converter</h1>

<p align="center">
  <strong>Spell any name using the NATO phonetic alphabet.</strong><br>
  A simple command-line application built with Python and Pandas.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Interface-CLI-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Command Line Interface">
</p>

---

## 📡 About the project

**NATO Phonetic Alphabet Converter** is a command-line program that converts a name into its corresponding NATO phonetic code words.

The application reads the NATO alphabet from a CSV file, creates a lookup dictionary with dictionary comprehension, and converts every letter entered by the user using list comprehension.

For example:

```text
Enter your name: Naza
['November', 'Alfa', 'Zulu', 'Alfa']
```

## ✨ Features

* Loads NATO phonetic alphabet data from a CSV file.
* Automatically converts user input to uppercase.
* Maps each letter to its NATO code word.
* Uses dictionary comprehension to create the alphabet lookup table.
* Uses list comprehension to convert the entered name.
* Supports every letter from `A` to `Z`.

## ⚙️ How it works

The CSV file is loaded into a Pandas DataFrame:

```python
df = pd.read_csv("nato_phonetic_alphabet.csv")
```

A dictionary is then created from the DataFrame:

```python
alphabet = {
    row.letter: row.code
    for index, row in df.iterrows()
}
```

Finally, each letter entered by the user is replaced with its NATO phonetic code:

```python
phonetic_name = [alphabet[letter] for letter in name]
```

## 🛠️ Technologies

* **Python 3** — program logic and user interaction.
* **Pandas** — reading and iterating through the CSV dataset.
* **CSV** — storing the NATO phonetic alphabet.

## 🧠 Concepts practiced

* Reading CSV files with Pandas.
* Working with DataFrames.
* Iterating over DataFrame rows with `.iterrows()`.
* Dictionary comprehension.
* List comprehension.
* Dictionary lookups.
* String manipulation with `.upper()`.
* Processing user input.

## 📁 Project structure

```text
nato-phonetic-alphabet/
├── main.py
├── nato_phonetic_alphabet.csv
└── README.md
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/nato-phonetic-alphabet.git
```

Enter the project directory:

```bash
cd nato-phonetic-alphabet
```

Install Pandas:

```bash
pip install pandas
```

Run the program:

```bash
python main.py
```

Make sure `nato_phonetic_alphabet.csv` is located in the same directory as `main.py`.

## ⚠️ Current limitation

The current version accepts letters from `A` to `Z`. Spaces, numbers, accented characters, and symbols will cause a `KeyError` because they are not present in the NATO alphabet dictionary.

## 🔮 Possible improvements

* Handle spaces and unsupported characters.
* Display a helpful message when the input is invalid.
* Allow the user to try again without restarting the program.
* Accept complete sentences instead of a single name.
* Format the converted output as a readable sentence.
* Add automated tests for valid and invalid input.

---

<p align="center">
  Built with Python while practicing Pandas and comprehension fundamentals.
</p>