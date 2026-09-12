# Fibonacci Series Generator

A simple and beginner-friendly Fibonacci Series Generator built using Python as part of my Python Development Internship at Crixsoft Solution.

## About the Project

The Fibonacci Series Generator is a Python program that generates the Fibonacci sequence based on the number of terms entered by the user.

In the Fibonacci sequence, each number is obtained by adding the two preceding numbers.

### Example

```text
0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
```

## Objective

The main objectives of this project are:

* Generate the Fibonacci series using Python.
* Practice Python loops and functions.
* Handle user input effectively.
* Implement basic input validation.
* Build a simple command-line application.

## Technologies Used

* Python 3
* Functions
* for loop
* Lists
* User Input
* Exception Handling

## How the Program Works

The program follows these steps:

1. The user enters the number of terms required.
2. The program starts with two numbers, `0` and `1`.
3. The next Fibonacci number is calculated by adding the previous two numbers.
4. The values are updated after every iteration.
5. The generated Fibonacci series is displayed on the screen.
6. Invalid input is handled using exception handling.

## Project Structure

```text
Fibonacci-Generator/
|
├── fibonacci.py
└── README.md
```

### fibonacci.py

Contains the complete Python source code for generating the Fibonacci series.

### README.md

Contains the project documentation and instructions.

## How to Run the Project

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

### 2. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 3. Open the Project Folder

```bash
cd Fibonacci-Generator
```

### 4. Run the Program

```bash
python fibonacci.py
```

## Example Output

### Example 1

```text
========================================
       FIBONACCI SERIES GENERATOR
========================================

Enter the number of terms: 10

Fibonacci Series:
0 → 1 → 1 → 2 → 3 → 5 → 8 → 13 → 21 → 34
```

### Example 2 - Invalid Input

```text
========================================
       FIBONACCI SERIES GENERATOR
========================================

Enter the number of terms: -5

Please enter a positive number.
```

## Fibonacci Logic

The Fibonacci sequence follows this rule:

```text
Next Number = Previous Number + Current Number
```

For example:

```text
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
```

Therefore:

```text
0 → 1 → 1 → 2 → 3 → 5 → 8 → 13
```

## Python Concepts Used

This project helped me practice the following Python concepts:

* Variables
* Functions
* Lists
* for loops
* range()
* User input
* Type conversion
* Conditional statements
* Exception handling
* Basic algorithm implementation

## Future Improvements

Some features that can be added in the future:

* Create a graphical user interface using Tkinter.
* Add an option to generate Fibonacci numbers up to a specific value.
* Add performance comparison between iterative and recursive approaches.
* Add additional input validation.
* Add a graphical representation of the Fibonacci sequence.

## Internship

This project was completed as part of my Python Development Internship at Crixsoft Solution.

Project: Fibonacci Series Generator

Domain: Python Development

## Author

Ganesula Pradeep Krishna

Python Developer | AI Enthusiast | Automation

## Acknowledgement

Thanks to Crixsoft Solution for providing this project opportunity and helping me gain practical experience in Python development.
