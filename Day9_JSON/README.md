# Day 9 – JSON in Python (14 July 2026)

## 📚 Topics Covered

- Introduction to JSON
- Python Dictionary vs JSON
- `json.dumps()`
- `json.loads()`
- `json.dump()`
- `json.load()`
- Reading and Writing JSON Files
- Working with List of Dictionaries
- Read → Modify → Write Pattern
- Refactoring Duplicate Code

---

## ✅ What I Learned

### JSON Basics

- JSON (JavaScript Object Notation) is a standard format used to store and exchange data.
- JSON looks very similar to a Python dictionary.
- Most APIs return data in JSON format.

---

### JSON Methods

#### `json.dumps()`
- Converts a Python object into a JSON string.

#### `json.loads()`
- Converts a JSON string back into a Python object (dictionary or list).

#### `json.dump()`
- Writes a Python object directly to a JSON file.

#### `json.load()`
- Reads JSON data from a file and converts it back into a Python object.

---

## ⭐ Important Concepts Learned

### JSON should have one root element

Invalid JSON:

```json
{}
{}
```

Valid JSON:

```json
[
    {},
    {}
]
```

A JSON file should contain either:
- One Object (`{}`)
- One Array (`[]`)

---

### Read → Modify → Write

When updating JSON data:

1. Read existing data.
2. Modify the data (Add / Update / Delete).
3. Write the updated data back to the file.

This pattern is used in most real-world applications.

---

### List of Dictionaries

When storing multiple records, use:

```python
[
    {
        "title": "...",
        "artist": "..."
    },
    {
        "title": "...",
        "artist": "..."
    }
]
```

instead of multiple standalone JSON objects.

---

### Refactoring

If the same code is repeated in multiple places, move it into a function.

Example:

```python
def load_songs():
    ...
```

```python
def save_songs(songs):
    ...
```

This makes the program cleaner and easier to maintain.

---

## 🛠 Mini Project

### Playlist Manager

Features:

- View Playlist
- Add Song
- Search Song
- Store songs in `songs.json`

Applied concepts:

- Functions
- JSON
- File Handling
- Lists
- Dictionaries
- Exception Handling
- Refactoring

---

## 💡 Key Takeaways

- JSON is the most common format used by APIs.
- After reading JSON in Python, it becomes a dictionary or list.
- Consistent data structures make programs simpler.
- Functions should return clear values (`True` / `False`) instead of relying on implicit returns.
- Removing duplicate code improves readability and maintainability.

---

## 🚀 Ready for Next Topic

Day 10 – APIs

Looking forward to learning how Python communicates with real-world services and works with live JSON responses.