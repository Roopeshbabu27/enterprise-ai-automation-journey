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

    choice = int(input("Enter your choice 1/2/3/4: "))
    #VIEW BOOKS
    if choice == 1:
        with open("books.txt") as f:
            books = f.readlines()
        
        counter = 1
        for book in books:
            print(f"Book {counter}: ", book.strip())
            counter +=1

    #ADD BOOK
    elif choice == 2:
        book_name = input("Enter Book Name: ")
        with open("books.txt", "a") as f:
            f.write(f"\n{book_name}")
        print("Book Added Successfully")
        

    #SEARCH BOOK
    elif choice == 3:
        book_name = input("Enter Book Name to Search: ")
        with open("books.txt") as f:
            books = [book.strip() for book in f.readlines()] 
            if book_name in books:
                print("Found")
            else:
                print("Not found")

    elif choice == 4:
        print("Thank you!")
        break
