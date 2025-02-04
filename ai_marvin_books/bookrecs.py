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


def get_mock_recommendations():
    # mock_recommendations = [Book(title='Doctor Sleep', author='Stephen King', year=2013), Book(title='The Haunting of Hill House', author='Shirley Jackson', year=1959), Book(title='Carrie', author='Stephen King', year=1974), Book(title='Pet Sematary', author='Stephen King', year=1983), Book(title='It', author='Stephen King', year=1986)]
    mock_recommendations = \
        [
            Book(title='Doctor Izzin', author='Stephen Fay King', year=2013),
            Book(title='Some Haunting Some Where', author='Michael Jackson', year=1999),
            Book(title='Carrie Me', author='Stephen Fay King', year=1974),
            Book(title='Pet Scritches', author='Stephen Fay King', year=1983),
            Book(title='What', author='Stephen Fay King', year=1986)
        ]
    return mock_recommendations


if __name__ == '__main__':

    print("::: BOOK RECS :::")
    print("::: Based on code by Bob Belderbos / PyBites :::")
    print(":::")

    ui_tweaking = True

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

    # print("===")
    # print(f"initial: {query_book}")
    print("===")

    if not ui_tweaking:
        recommendations = recommend_similar_books(query_book)
    else:
        recommendations = get_mock_recommendations()
    
    for book in recommendations:
        print(f"===>  {book.title} => {book.author} => {book.year}")

    # print("===")
    # print(f"returns: {recommendations}")
    print("===")

    print(":::")
    print("::: END :::")
    sys.exit()
