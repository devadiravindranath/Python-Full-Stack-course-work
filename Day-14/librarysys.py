library = []

#adding a book
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    book = {
        'id':book_id,
        'title':title,
        'author':author,
        'status':'Available'
        }
    library.append(book)
    print("Book added successfully!\n")


#checking books in the library

def view_book():
    if not library:
        print('No Books in library.\n')
        return
    print('\n----library Books---')
    for book in library:
        print(f"ID:{book['id']},Title:{book['title']},"
              f"Author:{book['author']},Status:{book['status']}")
    print()


def issue_book():
    book_id = input("Enter the book ID to issue: ")

    for book in library:
        if book['id'] == book_id:
            if book['status']== 'Available':
                book['status'] = 'Issued'
                print("Book Issued successfully!\n")
            else:
                print("Book Already Issued!\n ")
            return
    print("Book not found!! \n")


def return_book():
    book_id = input("Enter book ID to Retrun:")

    for  book in library:
        if book['id']==book_id:
            if book['status']== "Available":
                book['status']== "Issued"
                print("Book returned successfully\n")
            else:
                print("Book was not issued\n")
            return
    print("Book not found!\n")


while True:
    print("======LIBRARY MANAGEMENT MENU=======")
    print("1.Add Book")
    print("2.View Books")
    print("3.Issue Books")
    print("4.Return Book")
    print("5.Exit")


    choice=input("Enter the choice: ")
    if choice=="1":
        add_book()
    elif choice =="2":
        view_book()
    elif choice =="3":
        issue_book()
    elif choice =="4":
        return_book()
    elif choice =="5":
        print("Thank you!! Existing Library System.")
        break
    else:
        print("Invalid choice!!!! Try again.\n")
        
