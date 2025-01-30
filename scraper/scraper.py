import requests

urls = [
    "https://www.example.com",
    "https://www.invalid-url.com",
    "https://www.anotherexample.com"
]

def is_url_valid(url):
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e}")
        return False

for url in urls:
    if is_url_valid(url):
        print(f"{url} is valid.")
    else:
        print(f"{url} is not valid.")
