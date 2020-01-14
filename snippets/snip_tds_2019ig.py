#   Towards Data Science
#   30 Helpful Python Snippets That You Can Learn in 30 Seconds or Less
#   Fatos Morina
#   https://towardsdatascience.com/30-helpful-python-snippets-that-you-can-learn-in-30-seconds-or-less-69bb49204172
#

import sys
from snippets.all_unique import unique
from snippets.anagram import anagram

def main():
    print('(snippets) main:')
    print()

    x1 = [1,1,2,2,3,2,3,4,5,6]
    print(unique.is_all_unique(x1))

    print(anagram.is_anagram("abcd3", "3acdb"))

    print()
    print('(snippets) end::')

    return 0


# ----------------------------------------
if __name__ == '__main__':
    result0 = main()
    sys.exit(0)
