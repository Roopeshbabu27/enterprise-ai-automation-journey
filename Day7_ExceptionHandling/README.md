# Day 07 – Exception Handling

## 📅 Date
13-07-2026

---

# 📚 Topics Covered

- try
- except
- ValueError
- FileNotFoundError
- Input Validation
- Refactoring using Functions
- Menu Driven Application

---

# 📖 Concepts Learned

## try

Used to execute code that may generate an exception.

```python
try:
    number = int(input("Enter a number: "))
```

---

## except

Handles the exception without crashing the program.

```python
except ValueError:
    print("Please enter a valid number.")
```

---

## FileNotFoundError

```python
try:
    with open("books.txt") as f:
        data = f.read()
except FileNotFoundError:
    print("Books file not found.")
```

---

# 💻 Project

## Book Manager Version 2

### Features

- View Books
- Add Book
- Search Book
- Exit Application

---

## Improvements Made

- Refactored into functions
- Added exception handling
- Validated menu input
- Case-insensitive search
- Removed generic `except`
- Used specific exceptions
- Improved program structure

---

# 🧠 Key Learnings

- Use `try` for code that may fail.
- Catch only the expected exception.
- Avoid using generic `except`.
- Handle invalid user input gracefully.
- Handle missing files without crashing.
- Functions should have a single responsibility.

---

# ⭐ Important Concept

## Return vs Print

Use **return** when another function needs the result.

```python
def search_book(name):
    return True
```

Use **print** when the function's responsibility is displaying information.

```python
def view_books():
    print(book)
```

---

# 🚀 Next Topic

Modules (`import`)