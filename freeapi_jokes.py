import requests


def fetch_random_joke():
    response = requests.get(
        "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    )
    data = response.json()
    if data["success"] and "data" in data:
        joke_id = data["data"]["id"]
        joke = data["data"]["content"]
        return joke_id, joke
    else:
        raise Exception("Failed to fetch joke")


def main():
    try:
        joke_id, joke = fetch_random_joke()
        print(f"ID: {joke_id}")
        print(f"Joke: {joke}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
