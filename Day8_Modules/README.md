# Day 08 – Modules

## 📅 Date
14-07-2026

---

# 📚 Topics

- Python Modules
- import
- from ... import ...
- Organizing Code
- Splitting Programs into Multiple Files

---

# 📖 Concepts

A module is simply another Python file containing functions or variables that can be reused.

Example:

book_operations.py

```python
def view_books():
    print("Viewing Books")
```

book_manager.py

```python
import book_operations

book_operations.view_books()
```

---

# Folder Structure

```
Day08_Modules/

│
├── book_manager.py
├── book_operations.py
├── file_utils.py
├── books.txt
└── README.md
```

---

# Why Modules?

Instead of writing everything in one file:

```
500 lines
```

We divide the application into smaller reusable files.

Benefits:

- Better organization
- Easy maintenance
- Code reuse
- Cleaner projects
- Easier debugging

---

# Goal

Convert the Book Manager into a modular application by separating:

- Main Program
- Book Operations
- File Operations

---

# 🚀 Learning Outcome

Understand how Python projects are organized using modules and imports.