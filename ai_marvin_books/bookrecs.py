# ///
#
#
#
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

if __name__ == '__main__':

    print("::: BOOK RECS :::")
    print("::: Based on code by Bob Belderbos / PyBites :::")
    print(":::")

    print(":::")
    print("::: END :::")
    sys.exit()

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