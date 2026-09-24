<h1 align="center">🧮 Advanced CLI Calculator</h1>

<p align="center">
  <strong>Calculate, continue, recover, and keep track of every operation.</strong><br>
  A persistent command-line calculator built with Python, custom exceptions, and JSON history.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Storage-JSON-000000?style=for-the-badge&logo=json&logoColor=white" alt="JSON">
  <img src="https://img.shields.io/badge/Interface-CLI-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white" alt="Command Line Interface">
  <img src="https://img.shields.io/badge/Error%20Handling-Exceptions-E34F26?style=for-the-badge" alt="Exception Handling">
</p>

---

## 🧮 About the project

**Advanced CLI Calculator** is an interactive command-line calculator that performs arithmetic operations, allows users to continue calculating with the previous result, and stores successful operations in a persistent JSON history.

The program validates user input, handles mathematical errors without terminating, and uses a custom exception to reject unsupported operations.

Unlike a basic calculator that performs a single calculation and exits, this application maintains its state throughout the session and restores previous history when it starts again.

The project also includes a `catching-exceptions/` directory containing the exercises used to practice file handling, built-in exceptions, and manually raised errors before applying those concepts to the calculator.

---

## ✨ Features

* Supports integer and decimal numbers.
* Performs addition, subtraction, multiplication, division, modulo, and exponentiation.
* Continues calculating with the previous result.
* Starts a new calculation without restarting the application.
* Handles invalid numeric input.
* Prevents division and modulo by zero.
* Rejects unsupported operators through a custom exception.
* Stores successful operations in a list of dictionaries.
* Saves calculation history to a JSON file.
* Restores previous history when the program starts.
* Recovers gracefully from missing, empty, or invalid JSON files.
* Displays saved operations in a readable format.
* Creates `history.json` automatically when needed.

---

## ➗ Supported operations

| Operation      | Operator | Example       |
| -------------- | :------: | ------------- |
| Addition       |    `+`   | `5 + 3 = 8`   |
| Subtraction    |    `-`   | `10 - 4 = 6`  |
| Multiplication |    `*`   | `6 * 2 = 12`  |
| Division       |    `/`   | `15 / 3 = 5`  |
| Modulo         |    `%`   | `10 % 3 = 1`  |
| Exponentiation |   `**`   | `2 ** 4 = 16` |

---

## 🎮 Session controls

After completing an operation, the calculator presents four options:

| Option | Action                                        |
| :----: | --------------------------------------------- |
|   `y`  | Continue calculating with the previous result |
|   `n`  | Start a new calculation                       |
|   `h`  | Display the complete operation history        |
|   `q`  | Save the history and close the calculator     |

---

## 💻 Example session

```text
Please enter a number: 12
Please enter an operation: /
Please enter a number: 4

The result of the operation is 3.0

Would you like to keep operating with 3.0? (y/n/q/h): y
Please enter an operation: **
Please enter a number: 2

The result of the operation is 9.0

Would you like to keep operating with 9.0? (y/n/q/h): h

12.0 / 4.0 = 3.0
3.0 ** 2.0 = 9.0
```

---

## 🛡️ Error handling

The calculator handles several failure scenarios without unexpectedly terminating.

### Invalid numbers

If the user enters text where a number is expected, Python raises a `ValueError`. The application catches it and asks the user to try again.

```text
Please enter a number: hello
Please enter a valid number
```

### Division or modulo by zero

The calculator explicitly raises and catches `ZeroDivisionError` when the second operand is zero.

```text
Error occurred: Division by zero is not allowed
```

### Unsupported operations

Invalid operators are handled with a custom exception:

```python
class InvalidOperationError(Exception):
    pass
```

If the user enters an unsupported operator, the calculator raises `InvalidOperationError` with a descriptive message.

```text
& is not a valid operation
```

### Missing or damaged history

When the program starts, it attempts to load `history.json`.

If the file does not exist, is empty, or contains invalid JSON, the application safely begins with an empty history.

---

## 💾 JSON history

Every successful operation is represented as a dictionary:

```python
{
    "first_number": 12.0,
    "operation": "/",
    "second_number": 4.0,
    "result": 3.0
}
```

The dictionaries are stored inside a list and written to `history.json` when the user exits with `q`:

```json
[
    {
        "first_number": 12.0,
        "operation": "/",
        "second_number": 4.0,
        "result": 3.0
    },
    {
        "first_number": 3.0,
        "operation": "**",
        "second_number": 2.0,
        "result": 9.0
    }
]
```

The history file is generated locally and excluded from version control because it contains runtime data unique to each user.

---

## 🧠 Concepts practiced

* Functions and return values
* Positional arguments with `*args`
* Keyword arguments with `**kwargs`
* Conditional logic
* State management with `None`
* Continuous execution with `while`
* Input validation
* `try`, `except`, and `else`
* Built-in Python exceptions
* Creating and raising custom exceptions
* Lists of dictionaries
* JSON serialization and deserialization
* Reading and writing files with context managers
* Persistent application data
* Separation of calculation, recording, and display logic

---

## 🧪 Supporting exercises

The `catching-exceptions/` directory contains smaller exercises created before the main calculator implementation.

These exercises cover:

* Handling `FileNotFoundError`
* Creating missing files
* Handling `KeyError`
* Handling `IndexError`
* Using `try`, `except`, `else`, and `finally`
* Raising a `ValueError`
* Processing dictionaries with missing values

They provide the exception-handling foundation used by the calculator.

---

## 📁 Project structure

```text
21-Updated-Calculator/
├── catching-exceptions/
│   ├── exercises.py
│   └── README.md
├── art.py
├── main.py
└── README.md
```

The program generates `history.json` locally after the first completed session:

```text
21-Updated-Calculator/
├── catching-exceptions/
│   ├── exercises.py
│   └── README.md
├── art.py
├── main.py
├── README.md
└── history.json
```

The generated history file is listed in `.gitignore` and is not included in commits.

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/nazareno-urday/python-lab.git
```

Enter the project directory:

```bash
cd python-lab/01-foundations/21-Updated-Calculator
```

Run the calculator:

```bash
python main.py
```

No external packages are required.

---

## 🔮 Possible improvements

* Add automated tests with `pytest`.
* Save the history immediately after every successful operation.
* Add an option to clear saved history.
* Support unary operations such as square root.
* Add timestamps to history records.
* Refactor repeated input and exception-handling logic.
* Separate calculations, storage, and interface logic into modules.

---

<p align="center">
  Built with Python while practicing exception handling, state management, and JSON persistence.
</p>
