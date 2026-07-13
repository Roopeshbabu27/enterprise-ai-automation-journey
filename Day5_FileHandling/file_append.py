with open("notes.txt","a") as f:
    f.write("\nTomorrow I will learn JSON.")

with open("notes.txt") as f:
    print(f.read())
