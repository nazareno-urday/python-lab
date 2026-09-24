<h1 align="center">📡 NATO Phonetic Alphabet Converter</h1>

<p align="center">
  <strong>Spell any name using the NATO phonetic alphabet.</strong><br>
  A command-line application built with Python and Pandas.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Interface-CLI-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Command Line Interface">
  <img src="https://img.shields.io/badge/Error%20Handling-Exceptions-E34F26?style=for-the-badge" alt="Exception Handling">
</p>

---

## 📡 About the project

**NATO Phonetic Alphabet Converter** is a command-line program that converts a name into its corresponding NATO phonetic code words.

The application reads the NATO alphabet from a CSV file, creates a lookup dictionary using dictionary comprehension, and converts every letter entered by the user using list comprehension.

Invalid characters are handled with Python exceptions. If the user enters a number, space, symbol, or unsupported character, the program displays a helpful message and allows them to try again without terminating.

### Example

```text
Enter your name: Naza
['November', 'Alfa', 'Zulu', 'Alfa']
```

### Invalid input

```text
Enter your name: Naza123
Sorry, only letters from A to Z are allowed.
Enter your name:
```

---

## ✨ Features

* Loads NATO phonetic alphabet data from a CSV file.
* Automatically converts user input to uppercase.
* Maps each letter to its corresponding NATO code word.
* Uses dictionary comprehension to create the alphabet lookup table.
* Uses list comprehension to convert the entered name.
* Supports every letter from `A` to `Z`.
* Handles unsupported characters using `try` and `except`.
* Catches invalid dictionary lookups through `KeyError`.
* Allows the user to try again after entering invalid input.
* Prevents invalid input from terminating the application.

---

## ⚙️ How it works

The NATO alphabet data is loaded into a Pandas DataFrame:

```python
df = pd.read_csv("nato_phonetic_alphabet.csv")
```

A dictionary is created from the DataFrame using dictionary comprehension:

```python
alphabet = {
    row.letter: row.code
    for index, row in df.iterrows()
}
```

The user's input is converted to uppercase:

```python
name = input("Enter your name: ").upper()
```

Each letter is then replaced with its corresponding NATO phonetic code word:

```python
phonetic_name = [alphabet[letter] for letter in name]
```

If an unsupported character is used, the dictionary lookup raises a `KeyError`. The program catches that exception, displays an error message, and asks the user to try again:

```python
try:
    phonetic_name = [alphabet[letter] for letter in name]

except KeyError:
    print("Sorry, only letters from A to Z are allowed.")
    return generate_phonetic()

else:
    print(phonetic_name)
```

---

## 🛠️ Technologies

* **Python 3** — application logic, input processing, and exception handling.
* **Pandas** — reading and iterating through the CSV dataset.
* **CSV** — storing the NATO phonetic alphabet data.
* **Command Line Interface** — interacting with the user.

---

## 🧠 Concepts practiced

* Reading CSV files with Pandas.
* Working with Pandas DataFrames.
* Iterating over DataFrame rows with `.iterrows()`.
* Dictionary comprehension.
* List comprehension.
* Dictionary lookups.
* String manipulation with `.upper()`.
* Processing user input.
* Defining and calling functions.
* Exception handling with `try`, `except`, and `else`.
* Catching invalid dictionary keys with `KeyError`.
* Retrying an operation after invalid input.

---

## 📁 Project structure

```text
19-Nato-Alphabet/
├── dictionary_comprehension/
├── list_comprehension/
├── main.py
├── nato_phonetic_alphabet.csv
└── README.md
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/nazareno-urday/python-lab.git
```

Enter the project directory:

```bash
cd python-lab/01-foundations/19-Nato-Alphabet
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

---

## ⚠️ Input validation

The program accepts letters from `A` to `Z`.

Spaces, numbers, accented characters, and symbols are not included in the NATO alphabet dictionary. If one of these characters is entered, the program catches the resulting `KeyError`, displays a helpful message, and asks the user to enter another name.

For example, `NAZA` is valid, while `NAZA URDAY`, `NAZA123`, or `NAZÁ` will request another attempt.

---

## 🔮 Possible improvements

* Replace recursive retries with a loop.
* Ignore spaces to support full names.
* Accept complete words and sentences.
* Handle accented characters by normalizing the input.
* Format the result as a readable sentence instead of a Python list.
* Add automated tests for valid and invalid input.
* Add an option to convert multiple names in one session.

---

<p align="center">
  Built with Python while practicing Pandas, comprehensions, and exception handling.
</p>
