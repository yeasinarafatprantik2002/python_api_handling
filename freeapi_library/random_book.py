import requests


def ran_book():
    try:
        response = requests.get(
            "https://api.freeapi.app/api/v1/public/books/book/random"
        )
        data = response.json()
        if data["success"] and "data" in data:
            books = data["data"]
            return books
        else:
            raise Exception("Failed to fetch books")

    except Exception as e:
        print(f"Error: {str(e)}")
        return []
