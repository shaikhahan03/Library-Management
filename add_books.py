from utils import books


def add_books():
    book_name = input("Enter the name of the book: ").strip().upper()
    books.append(book_name)
    print(f"'{book_name}' has been added to the library.")
