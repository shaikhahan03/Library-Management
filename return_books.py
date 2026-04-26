from utils import books, issued_books

def return_books():
    if len(issued_books) == 0:
        print("No books have been issued.")
    else:
        book_name = input("Enter the name of the book to return: ").strip().upper()
        if book_name in issued_books:
            issued_books.remove(book_name)
            books.append(book_name)
            print(f"'{book_name}' has been returned to the library.")
        else:
            print(f"'{book_name}' was not issued from the library.")
