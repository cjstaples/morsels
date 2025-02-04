# /// script
# dependencies = [
#   "marvin",
# ]
# ///

#   Book Recs via AI
#   Based on code by Bob Belderbos / PyBites
#

import os
import sys
import argparse

from pydantic import BaseModel, Field
import marvin

if "MARVIN_OPENAI_API_KEY" not in os.environ:
    sys.exit("Environment variable 'MARVIN_OPENAI_API_KEY' must be set before use")

class Book(BaseModel):
    title: str = Field(..., description="Title of Book")
    author: str = Field(..., description="Author of Book")
    year: int | None = Field(None, description="Year of Book Publication")

@marvin.fn
def recommend_similar_books(query_book: Book) -> list[Book]:
    """
    Given a Book object, return a list of similar books.
    Recommendations should consider similar genres.
    """

if __name__ == '__main__':

    print("::: BOOK RECS :::")
    print("::: Based on code by Bob Belderbos / PyBites :::")
    print(":::")

    parser = argparse.ArgumentParser(
        description="Recommend similar books using OpenAI"
    )
    parser.add_argument("--title", required=True, help="Book title")
    parser.add_argument("--author", required=True, help="Book author")
    args = parser.parse_args()

    print(f"book title => {args.title}")
    print(f"book author => {args.author}")

    query_book = Book(
        title=args.title,
        author=args.author,
        # year=int(args.year) if args.year else None,
    )
    recommendations = recommend_similar_books(query_book)
    for book in recommendations:
        print(f"{book.title} => {book.author} => {book.year}")

    print("===")
    print(f"initial: {query_book}")
    print("===")


    print(f"returns: {query_book}")
    print("===")

    print(":::")
    print("::: END :::")
    sys.exit()
