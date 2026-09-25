<h1 align="center">🫧 Bubble Sort</h1>

<p align="center">
  <strong>Compare. Swap. Repeat.</strong><br>
  A simple implementation of the Bubble Sort algorithm in Python.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Algorithm-Bubble%20Sort-00BFFF?style=for-the-badge" alt="Bubble Sort">
  <img src="https://img.shields.io/badge/Complexity-O(n²)-FF8C00?style=for-the-badge" alt="Time Complexity">
</p>

---

## 📌 About the project

This project implements the **Bubble Sort algorithm** using Python.

The program asks the user how many elements they want to sort, collects each number through the terminal, and arranges the complete list in ascending order.

It was developed to practice sorting algorithms, nested loops, list manipulation, comparisons, and manual value swapping.

## ⚙️ How Bubble Sort works

Bubble Sort repeatedly compares two neighboring elements.

If the element on the left is greater than the element on the right, their positions are swapped.

For example:

```text
Initial list: [5, 2, 4, 1]

Compare 5 and 2 → swap
[2, 5, 4, 1]

Compare 5 and 4 → swap
[2, 4, 5, 1]

Compare 5 and 1 → swap
[2, 4, 1, 5]
```

After the first complete pass, the largest value has moved to the end of the list. The process is repeated until every element is correctly ordered.

## ✨ Features

* Accepts a custom number of elements.
* Reads every value from the terminal.
* Sorts integer values in ascending order.
* Performs the sorting manually without using Python's `sort()` or `sorted()`.
* Uses nested loops to compare neighboring elements.
* Swaps values using a temporary variable.
* Displays the final sorted list.

## 💻 Example

```text
Enter number of elements: 5
Enter element: 9
Enter element: 3
Enter element: 7
Enter element: 1
Enter element: 5

Sorted elements: [1, 3, 5, 7, 9]
```

## 🧠 Concepts practiced

* Sorting algorithms
* Nested `for` loops
* Python lists
* User input
* Integer conversion
* List indexing
* Conditional statements
* Swapping values
* Algorithmic thinking

## 📊 Complexity

| Case             | Time complexity |
| ---------------- | --------------: |
| Best case        |         `O(n²)` |
| Average case     |         `O(n²)` |
| Worst case       |         `O(n²)` |
| Space complexity |          `O(1)` |

This implementation performs the same number of comparison passes even when the list is already sorted. It uses constant additional memory because the elements are rearranged directly inside the original list.

## 📁 Project structure

```text
bubble-sort/
├── bubble_sort.py
└── README.md
```

## 🚀 How to run

Clone the repository:

```bash
git clone https://github.com/your-username/bubble-sort.git
```

Enter the project directory:

```bash
cd bubble-sort
```

Run the program:

```bash
python main.py
```

No external libraries are required.

## 🔮 Possible improvements

* Stop early when no swaps occur during a complete pass.
* Reduce the number of comparisons after each pass.
* Support decimal values.
* Allow the user to choose between ascending and descending order.
* Display every sorting pass step by step.
* Compare its performance with other sorting algorithms.

---

<p align="center">
  Built with Python while learning data structures and algorithms.
</p>
