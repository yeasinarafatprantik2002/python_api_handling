from books_list import list_books
from book_desc import book_desc
from random_book_sugg import random_book


def main():
    print("Welcome to FreeAPI Library!\n")
    while True:
        print("//-FreeAPI Library-\\\\")
        print("1. List Books")
        print("2. Get random Book suggestion")
        print("3. Read Description")
        print("q. Quit")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_books()
            case "2":
                random_book()
            case "3":
                book_id = input("Enter book ID: ")
                book_desc(book_id)
            case "q":
                print("\nGoodbye!\n")
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
