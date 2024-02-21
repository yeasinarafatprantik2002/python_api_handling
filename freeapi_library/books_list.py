from books import fetch_books


def list_books():
    books = fetch_books()
    print("\nList of books:")
    print("*" * 107 + "\n")
    for book in books:
        print(f"ID: {book['id']}")
        print(f"Title: {book['volumeInfo']['title']}")
        print(f"Authors: {book['volumeInfo']['authors']}")
        print(f"Published Date: {book['volumeInfo']['publishedDate']}")
        print("\n" + "*" * 107 + "\n")
