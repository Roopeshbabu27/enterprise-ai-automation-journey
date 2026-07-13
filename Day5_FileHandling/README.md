# Day 05 – File Handling

## 📅 Date
13-07-2026

---

# 📚 Topics Covered

- File Handling
- Reading Files (`read()`)
- Reading Files Line by Line (`readlines()`)
- Writing to Files (`w`)
- Appending to Files (`a`)
- Using `with open()`
- File Iteration
- Converting File Data to Integers
- Basic File Reports

---

# 📖 Concepts Learned

### Reading a File

```python
with open("notes.txt") as f:
    print(f.read())
```

---

### Writing to a File

```python
with open("notes.txt", "w") as f:
    f.write("Today I learned File Handling in Python.")
```

---

### Appending to a File

```python
with open("notes.txt", "a") as f:
    f.write("\nTomorrow I will learn JSON.")
```

---

### Reading Multiple Lines

```python
with open("movies.txt") as f:
    movies = f.readlines()
```

---

### Iterating Through a File

```python
with open("movies.txt") as f:
    counter = 1
    for movie in f:
        print(f"Movie {counter}: {movie.strip()}")
        counter += 1
```

---

# 💻 Programs Completed

## ✅ Program 1 – Read File

- Read complete file using `read()`

---

## ✅ Program 2 – Write File

- Overwrite file contents

---

## ✅ Program 3 – Append File

- Append new data without deleting existing content

---

## ✅ Challenge 1 – Movies Report

Read movie names from a file and display:

```
Movie 1: Interstellar
Movie 2: Inception
Movie 3: Avatar
Movie 4: The Dark Knight
```

---

## ✅ Challenge 2 – Student Marks Report

Read marks from a file and display:

- Student-wise marks
- Total Marks
- Average Marks
- Highest Marks
- Lowest Marks

---

# 🧠 Key Learnings

- `read()` returns the complete file as a string.
- `readlines()` returns a list of lines.
- A file object can be directly used in a `for` loop.
- `"w"` overwrites existing content.
- `"a"` appends new content.
- `with open()` automatically closes the file.
- Data read from files is stored as strings and often needs type conversion (e.g., `int()`).

---

# 💡 Reflection

### What was easy?

Reading, writing, and appending files were straightforward after understanding the different file modes.

### What was confusing?

Initially, I forgot that data read from files is stored as strings. This caused an issue while using `max()` and `min()`. After converting the values to integers, everything worked correctly.

### Where will I use File Handling?

- Reading configuration files
- Processing CSV/TXT reports
- Storing application data
- Reading prompts for AI
- Summarizing documents using AI
- Automation scripts that generate reports

---

# ⭐ Overall Progress

- ✅ Python Fundamentals
- ✅ Strings
- ✅ Conditions
- ✅ Loops
- ✅ Lists
- ✅ Dictionaries
- ✅ Functions
- ✅ File Handling (Basics)

---

## 🚀 Next Topic

**File Handling Project + JSON**