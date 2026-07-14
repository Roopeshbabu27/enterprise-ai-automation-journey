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

def main():
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
            choice = int(input("Enter a choice 1/2/3/4: "))
            if 1 <= choice <= 4:
                if choice == 1:
                    view_books()
                elif choice == 2:
                    book = input("Enter Book Name: ")
                    add_book(book)
                elif choice == 3:
                    book = input("Enter a book name to search: ").strip().lower()
                    if search_book(book):
                        print("Found")
                    else:
                        print("Not Found")
                elif choice == 4:
                    break
            else:
                print("Invalid choice")
        except ValueError:
            print("Enter a valid number")    

main()



'''
#Challenge 1 Safe Division
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
try:
    res = first / second
    print(res)
except ZeroDivisionError:
    print("Cannot divide by zero")


#Challenge 2 – Valid Number Input
try:
    msg = int(input("Enter Age: "))
except:
    print("Enter a valid number")
    
#Challenge 3 File Not Found
try:
    with open("student.txt") as f:
        print(f.read())
except:
    print("File not found.")
'''