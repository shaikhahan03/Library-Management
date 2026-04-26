import add_books
import show_books
import issue_books
import return_books


def library():
    while True:
        print("\n1. Add Books")
        print("2. View Books")
        print("3. Issue Books")
        print("4. Return Books")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                add_books.add_books()
            elif choice == 2:
                show_books.show_books()
            elif choice == 3:
                issue_books.issue_books()
            elif choice == 4:
                return_books.return_books()
            elif choice == 5:
                print("Thank you for using the library system.")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    library()
