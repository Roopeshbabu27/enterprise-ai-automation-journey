import book_operations
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
                    book_operations.view_books()
                elif choice == 2:
                    book = input("Enter Book Name: ")
                    book_operations.add_book(book)
                elif choice == 3:
                    book = input("Enter a book name to search: ").strip().lower()
                    if book_operations.search_book(book):
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