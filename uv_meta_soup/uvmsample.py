# ///
# dependencies = [
#   "bs4",
#   "httpx",
#   "typer"
# ]
# ///

#   uv / metadata sample
#   Based on code by Bob Belderbos / PyBites
#

import sys
import textwrap

from bs4 import BeautifulSoup
import httpx
import typer

app = typer.Typer()
ui_tweaking = True

BASE_URL = "https://www.googleapis.com/books/v1/volumes"
BOOK_URL = BASE_URL + "/{}"
SEARCH_URL = BASE_URL + "?q={}&langRestrict=en"


def search_books(term: str):
    """Search books by term."""
    query = SEARCH_URL.format(term)
    resp = httpx.get(query)
    resp.raise_for_status()

    books = []
    for item in resp.json().get("items", []):
        try:
            google_id = item["id"]
            title = item["volumeInfo"]["title"]
            books.append((google_id, title))
        except KeyError:
            continue

    return books


def get_book_details(book_id: str):
    """Retrieve details for a specific book."""
    book_url = BOOK_URL.format(book_id)
    resp = httpx.get(book_url)
    resp.raise_for_status()
    return resp.json().get("volumeInfo", {})


def clean_and_shorten_description(description: str, max_length: int = 300):
    """Remove HTML Tags from the description and truncate it."""
    plain_text = BeautifulSoup(description, "html.parser").get_text()
    return textwrap.shorten(plain_text, width=max_length, placeholder="...")

@app.command()
def search(terms: list[str] = typer.Argument(..., help="Book Search Terms")):
    search_string = " ".join(terms)
    books = search_books(search_string)

    if not books:
        typer.echo("No books found.")
        raise typer.Exit()

    typer.echo("Books found:")
    for idx, (book_id, title) in enumerate(books, start=1):
        typer.echo(f"{idx}, {title}")


if __name__ == '__main__':
    print("::: UV METADATA SAMPLE :::")
    print("::: Based on code by Bob Belderbos / PyBites :::")
    print(":::")

    print("===")
    app()
    print("===")

    print(":::")
    print("::: END :::")
    sys.exit()
