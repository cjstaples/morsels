# ///
# dependencies = [
#   "bs4",
#   "httpx",
#   "typer"
# ]
# ///

#   uv / metadata example
#   using sample google api book search typer app
#
#   Based on code by Bob Belderbos / PyBites
#   https://pybit.es/articles/create-project-less-python-utilities-with-uv-and-inline-script-metadata/

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

    typer.echo("----------------------------------------")
    typer.echo(f"--  searching for: [ {search_string} ]")
    typer.echo("----------------------------------------")
    if not books:
        typer.echo("No books found.")
        raise typer.Exit()

    typer.echo("Books found:")
    for idx, (book_id, title) in enumerate(books, start=1):
        typer.echo(f"*  {idx} :: {title}")

    typer.echo("----------------------------------------")
    selection = typer.prompt(
        "Enter the number of the book you want details for:", type=int
    )
    if selection < 1 or selection > len(books):
        typer.echo("* Invalid selection *")
        raise typer.Exit()

    selected_book_id = books[selection - 1][0]
    typer.echo("...fetching details...")

    details = get_book_details(selected_book_id)
    typer.echo("\n*** Book Details ***")
    typer.echo(f"Title:              {details.get('title', 'n/a')}")
    typer.echo(f"Subtitle:           {details.get('subtitle', 'n/a')}")
    typer.echo(f"Authors:            {', '.join(details.get('authors', []))}")
    typer.echo(f"Publisher:          {details.get('publisher', 'n/a')}")
    typer.echo(f"Published Date:     {details.get('publishedDate', 'n/a')}")
    description = details.get("description", "n/a")
    typer.echo(f"Description:        {clean_and_shorten_description(description, max_length=80)}")


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
