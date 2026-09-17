<h1 align="center">📨 Mail Merge</h1>

<p align="center">
  <strong>Read. Personalize. Generate.</strong><br>
  An automated letter generator built with Python.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Concept-File%20Handling-2E8B57?style=for-the-badge" alt="File Handling">
  <img src="https://img.shields.io/badge/Type-Automation-8A2BE2?style=for-the-badge" alt="Automation">
</p>

---

## 📬 About the project

A simple mail merge automation tool developed with Python.

The program reads a list of invited guests, replaces the `[name]` placeholder inside a letter template, and generates a personalized invitation for every person automatically.

Instead of writing each invitation manually, the program creates all the required letters in just one execution.

## ⚙️ How it works

1. Reads the guest names from `invited_names.txt`.
2. Loads the invitation template from `starting_letter.txt`.
3. Replaces the `[name]` placeholder with each guest's name.
4. Creates a separate personalized letter for every guest.
5. Saves the generated letters inside the `ReadyToSend` folder.

## ✨ Features

- Reads information from external text files
- Processes multiple guest names automatically
- Replaces placeholders with personalized data
- Generates one invitation per guest
- Preserves the original letter structure
- Organizes generated files in a dedicated output folder
- Uses only Python's standard library
- Demonstrates practical file-handling automation

## 🧩 Project structure

```text
17-Mail-Merge/
├── main.py
├── Input/
│   ├── Names/
│   │   └── invited_names.txt
│   └── Letters/
│       └── starting_letter.txt
├── Output/
│   └── ReadyToSend/
│       ├── letter_for_Aang.txt
│       ├── letter_for_Zuko.txt
│       ├── letter_for_Appa.txt
│       ├── letter_for_Katara.txt
│       ├── letter_for_Sokka.txt
│       ├── letter_for_Momo.txt
│       ├── letter_for_Uncle Iroh.txt
│       └── letter_for_Toph.txt
└── README.md
```

## 📝 Letter template

The program uses `[name]` as the placeholder that will be replaced with each guest's name.

```text
Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Nazareno
```

## 📤 Example output

For the guest `Aang`, the program generates:

```text
Dear Aang,

You are invited to my birthday this Saturday.

Hope you can make it!

Nazareno
```

The result is saved as:

```text
Output/ReadyToSend/letter_for_Aang.txt
```

## 🚀 Getting started

### Requirements

- Python 3.x
- No external libraries required

### Run the project

Clone the repository and move into the project directory:

```bash
git clone https://github.com/nazareno-urday/python-lab.git
cd python-lab/17-Mail-Merge
```

Run the program:

```bash
python main.py
```

The personalized invitations will be generated automatically inside:

```text
Output/ReadyToSend/
```

## 🧠 Concepts practiced

This project reinforces several important Python fundamentals:

- Reading text files with `open()`
- Writing and creating new files
- Using context managers with `with`
- Working with lists
- Iterating with `for` loops
- Cleaning strings with `strip()`
- Replacing text with `replace()`
- Using formatted strings
- Organizing input and output directories
- Automating repetitive tasks

## 🛠️ Built with

- **Python 3**
- **File I/O**
- **String manipulation**
- **Automation logic**

---

<p align="center">
  Made with Python by <strong>Nazareno</strong>
</p>