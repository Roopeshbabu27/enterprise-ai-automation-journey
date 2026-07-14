def view_books():
    try:
        with open("books.txt") as f:
                books = f.readlines()
            
        counter = 1
        for book in books:
            print(f"Book {counter}: ", book.strip())
            counter +=1
    except FileNotFoundError:
        print("File not found")


def add_book(book_name):
    with open("books.txt", "a") as f:
        f.write(f"\n{book_name}")
    print("Book Added Successfully")

def search_book(book_name):
    try:
        with open("books.txt") as f:
            books = [book.strip().lower() for book in f.readlines()] 
            return book_name in books              
    except FileNotFoundError:
        print("Books file not found")
