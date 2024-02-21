import requests


def fetch_books():
    try:
        response = requests.get(
            "https://api.freeapi.app/api/v1/public/books?page=1&limit=10&inc=kind%2Cid%2Cetag%2CvolumeInfo&query=tech"
        )
        data = response.json()
        if data["success"] and "data" in data:
            books = data["data"]["data"]
            return books
        else:
            raise Exception("Failed to fetch books")

    except Exception as e:
        print(f"Error: {str(e)}")
        return []
