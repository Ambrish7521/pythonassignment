# pythonassignment
# Python Algorithms Collection  
This repository contains two Python programs:

1. **N-Queens Solver** – Uses backtracking to generate all valid solutions.
2. **Custom Regex Pattern Matcher** – Implements a simple pattern-matching system with `+` support.

Both programs are fully documented below.

---

# 🧩 1. N-Queens Solver

This program solves the classic **N-Queens problem**, where you must place `N` queens on an `N×N` chessboard so that none of them attack each other.

## 🛠️ Features
- Backtracking algorithm  
- Counts all valid solutions  
- Displays each board configuration  
- Works for any integer `N ≥ 1`

---

## 🧠 How It Works
The solver uses:
- `used_columns` → tracks blocked columns  
- `used_diag1` → tracks `row - col` diagonals  
- `used_diag2` → tracks `row + col` diagonals  

Whenever a queen is placed, these sets ensure no other queen can attack it.

---

## ▶️ Example Run
