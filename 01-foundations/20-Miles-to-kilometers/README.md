<h1 align="center">📏 Miles to Kilometers Converter</h1>

<p align="center">
  <strong>Convert miles into kilometers through a simple desktop interface.</strong><br>
  A graphical application built with Python and Tkinter.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-2C3E50?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/Interface-Desktop-4EAA25?style=for-the-badge" alt="Desktop Interface">
</p>

---

## 📏 About the project

**Miles to Kilometers Converter** is a desktop application that converts a distance entered in miles into its equivalent value in kilometers.

The program uses Tkinter to create a graphical interface containing an input field, descriptive labels, a result display, and a button that performs the conversion.

For example:

```text
Miles: 10
Kilometers: 16.09
```

The conversion is calculated using the following formula:

```text
kilometers = miles × 1.609
```

## ✨ Features

* Accepts a distance entered in miles.
* Converts the entered value into kilometers.
* Displays the result directly in the application window.
* Uses a button callback to perform the calculation.
* Organizes interface elements with Tkinter's grid layout.
* Requires no external Python packages.

## ⚙️ How it works

The program creates the main application window:

```python
window = tk.Tk()
window.minsize(300, 200)
window.title("Miles to Kilometers")
```

The value entered by the user is read from the input field and converted into an integer:

```python
entry.get()
```

When the user presses the **Calculate** button, the callback function performs the conversion and updates the result label:

```python
def click():
    result_label.config(text=(int(entry.get()) * 1.609))
```

The button is connected to the function through its `command` argument:

```python
button = tk.Button(
    text="Calculate",
    command=click,
    font=("Times New Roman", 12, "bold")
)
```

Finally, Tkinter's event loop keeps the application running and waiting for user interaction:

```python
window.mainloop()
```

## 🛠️ Technologies

* **Python 3** — application logic and mathematical conversion.
* **Tkinter** — graphical user interface.
* **Grid geometry manager** — positioning widgets inside the window.

## 🧠 Concepts practiced

* Creating desktop applications with Tkinter.
* Working with windows, labels, entries, and buttons.
* Positioning widgets using `.grid()`.
* Reading text from an entry widget with `.get()`.
* Updating widget properties with `.config()`.
* Connecting buttons to callback functions.
* Converting strings into integers.
* Applying a mathematical conversion formula.
* Working with an event-driven program.

## 📁 Project structure

```text
miles-to-kilometers-converter/
├── main.py
└── README.md
```

## 🚀 Installation

Clone or download the repository and enter the project directory.

No external dependencies are required because Tkinter is included with most standard Python installations.

Run the application:

```bash
python main.py
```

Enter a value in miles and press **Calculate** to display the equivalent distance in kilometers.

## ⚠️ Current limitations

* The current version only accepts whole numbers because the input is converted with `int()`.
* Empty or non-numeric input will produce a `ValueError`.
* Results are displayed without controlling the number of decimal places.
* The application only converts from miles to kilometers.

## 🔮 Possible improvements

* Accept decimal values using `float()`.
* Validate the input before performing the conversion.
* Display a helpful message when the input is invalid.
* Round the result to two decimal places.
* Add kilometers-to-miles conversion.
* Improve the visual design with colors and spacing.
* Allow the user to press `Enter` to calculate.
* Add automated tests for the conversion logic.

---

<p align="center">
  Built with Python while practicing Tkinter and event-driven programming.
</p>
