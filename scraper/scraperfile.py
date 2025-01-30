#   URL Checker for Company Careers sites
#   based on AI generated code

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls


def is_url_valid(url, session):
    try:
        response = session.get(url, timeout=5)  # Set timeout to 5 seconds
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Error checking {url}: {e}")
        return False


def verify_base_url(url, session):
    print(f"verifying {url}...")
    return is_url_valid(url, session)


def verify_base_careers_url(url, session):
    url_careers = url + '/careers'
    print(f"::  verifying careers {url_careers}...")
    return is_url_valid(url_careers, session)


def main():
    file_path = 'urls.txt'  # Path to the text file containing URLs
    urls = read_urls_from_file(file_path)

    # Configure retries
    retry_strategy = Retry(
        total=3,  # Total number of retries
        status_forcelist=[429, 500, 502, 503, 504],  # Retry on these status codes
        # method_whitelist=["HEAD", "GET", "OPTIONS"]  # Retry for these HTTP methods
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    base_valid = False

    for url in urls:
        base_valid = verify_base_url(url, session)

        if base_valid:
            print(f"::  {url} is valid.")
            base_careers_valid = verify_base_careers_url(url, session)
            if base_careers_valid:
                print(f"::  {url}/careers is valid!")


        else:
            print(f"::  {url} is invalid. Not checking sub urls.")

        print(f"-" * 60)


if __name__ == "__main__":
    main()