from utils import books


def show_books():
    if len(books) == 0:
        print("No books in the library.")
    else:
        print("Available Books in the library:")
        for book in books:
            print(f"- {book}")
