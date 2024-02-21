import requests


def book_details(book_id):
    try:
        response = requests.get(
            f"https://api.freeapi.app/api/v1/public/books/{book_id}"
        )
        data = response.json()
        if data["success"] and "data" in data:
            book = data["data"]["volumeInfo"]
            return book
        else:
            raise Exception("Failed to fetch book")
    except Exception as e:
        print(f"Error: {str(e)}")
        return {}
