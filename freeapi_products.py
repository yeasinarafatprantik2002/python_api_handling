import requests


def fetch_random_product():
    response = requests.get(
        "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    )
    data = response.json()
    if data["success"] and "data" in data:
        product = data["data"]["data"]
        return product
    else:
        raise Exception("Failed to fetch product")


def main():
    try:
        product = fetch_random_product()
        print(f"\nTotal products: {len(product)}")
        print("\n" + "*" * 50 + "\n")
        for p in product:
            print(f"ID: {p['id']}")
            print(f"Title: {p['title']}")
            print(f"Category: {p['category']}")
            print(f"Price: {p['price']}")
            print("\n" + "*" * 50 + "\n")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
