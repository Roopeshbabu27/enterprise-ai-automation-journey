with open("notes.txt","w") as f:
    f.write("Today I learned File Handling in Python.")

with open("notes.txt") as f:
    print(f.read())
