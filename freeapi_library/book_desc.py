from book_details import book_details


def book_desc(book_id):
    book = book_details(book_id)
    print(f"\nBook details for book ID: {book_id}")
    print("*" * 107 + "\n")
    print(f"Title: {book['title']}")
    print(f"Authors: {book['authors']}")
    print(f"Published Date: {book['publishedDate']}\n")
    print(f"Description: {book['description']}")
    print("\n" + "*" * 107 + "\n")
