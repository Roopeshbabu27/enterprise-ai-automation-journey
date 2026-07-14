def view_books():
    with open("books.txt") as f:
            books = f.readlines()
        
    counter = 1
    for book in books:
        print(f"Book {counter}: ", book.strip())
        counter +=1

def add_book(book_name):
    with open("books.txt", "a") as f:
        f.write(f"\n{book_name}")
    print("Book Added Successfully")

def search_book(book_name):
    try:
        with open("books.txt") as f:
            books = [book.strip() for book in f.readlines()] 
            if book_name in books:
                print("Found")
            else:
                print("Not found")
    except:
        print("Books file not found")

def main():
    pass

while True:
    print(   
    '''
    ======== Book Manager ========
    1. View Books
    2. Add Book
    3. Search Book
    4. Exit
    '''
    )
    
    try:
        choice = int(input("Enter ur choice: "))
        break
    except:
        print("Enter a valid number")

