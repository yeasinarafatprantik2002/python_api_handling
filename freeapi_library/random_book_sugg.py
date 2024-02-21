from random_book import ran_book


def random_book():
    book = ran_book()
    print("\nRandom Book suggestion:")
    print("*" * 107 + "\n")
    print(f"ID: {book['id']}")
    print(f"Title: {book['volumeInfo']['title']}")
    print(f"Authors: {book['volumeInfo']['authors']}")
    print(f"Published Date: {book['volumeInfo']['publishedDate']}")
    print("\n" + "*" * 107 + "\n")
