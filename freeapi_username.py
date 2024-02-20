import requests


def fetch_random_user():
    response = requests.get(
        "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    )
    data = response.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user")


def main():
    try:
        username, country = fetch_random_user()
        print(f"Username: {username}")
        print(f"Country: {country}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
