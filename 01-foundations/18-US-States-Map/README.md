<h1 align="center">🗺️ U.S. States Game</h1>

<p align="center">
  <strong>How many U.S. states can you name?</strong><br>
  An interactive geography game built with Python, Turtle, and Pandas.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-Turtle-2E8B57?style=for-the-badge" alt="Turtle">
  <img src="https://img.shields.io/badge/Data-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
</p>

---

## 🎮 About the game

**U.S. States Game** is an interactive map challenge where the player must identify all 50 states of the United States.

Each correct answer is displayed directly on the map using coordinates stored in a CSV file. The game tracks the player's score, prevents duplicate answers, and generates a personalized study list containing every state that was missed.

## ✨ Features

* Interactive state input using Turtle dialog boxes.
* Automatic capitalization of player answers.
* Validation against a dataset containing all 50 states.
* Correct state names displayed at their map coordinates.
* Live score displayed as `correct answers / 50`.
* Duplicate-answer detection.
* Option to leave the game by entering `Exit`.
* Automatic generation of a `missing_states.csv` study file.

## 🕹️ How to play

1. Run the program.
2. Enter the name of a U.S. state.
3. Every correct answer will appear in its corresponding position on the map.
4. Continue until you identify all 50 states.
5. Enter `Exit` whenever you want to stop playing.

An incorrect answer ends the current game. If the game ends before completing all 50 states, the program creates a CSV file containing the states that were not guessed.

## 📚 Personalized study list

After exiting or entering an incorrect answer, the program generates:

```text
missing_states.csv
```

Example:

```csv
,states
0,Alaska
1,Arizona
2,Arkansas
```

This makes it possible to review the missing states before playing again.

## 🛠️ Technologies

* **Python 3** — game logic and data processing.
* **Turtle** — graphical interface, map display, and text placement.
* **Pandas** — CSV reading, DataFrame filtering, and file export.

## 🧠 Concepts practiced

* Reading and writing CSV files.
* Creating and filtering Pandas DataFrames.
* Working with lists.
* Membership checks using `in` and `not in`.
* Functions and loops.
* Conditional logic.
* Coordinate-based positioning.
* Score tracking.
* Duplicate-answer prevention.
* Basic data persistence.

## 📁 Project structure

```text
us-states-game/
├── main.py
├── 50_states.csv
├── blank_states_img.gif
├── missing_states.csv
└── README.md
```

> `missing_states.csv` is generated automatically after an unfinished game.

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/us-states-game.git
```

Enter the project directory:

```bash
cd us-states-game
```

Install Pandas:

```bash
pip install pandas
```

Run the game:

```bash
python main.py
```

Make sure `50_states.csv` and `blank_states_img.gif` are located in the same directory as the Python script.

## 🔮 Possible improvements

* Allow multiple incorrect attempts.
* Add a timer and personal best scores.
* Display hints for difficult states.
* Add regional game modes.
* Add different difficulty levels.
* Save previous scores between sessions.

---

<p align="center">
  Built with Python while practicing data analysis and GUI fundamentals.
</p>
