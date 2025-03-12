#  string cleaning
#  https://www.linkedin.com/pulse/5-python-tricks-you-wish-knew-earlier-benjamin-bennett-alexander-tbzxe/
#

import sys
import string

# ---------------

def main():
    print('(string cleaning) main:')
    print()

    input_string_1 = "#%^$#Something, to. learn- Python with&^$%$%#"
    input_string_2 = "#%^$#Something, else** to. learn- Python more with&^$%$%#"

    # make a translation table, mapping away all punctuation characters to nothing
    # works with other subsets of string.xxx e.g. string.ascii_letters or string.whitespace
    # translation_table = str.maketrans('', '', string.ascii_letters)

    translation_table_punc = str.maketrans('', '', string.punctuation)
    translation_table_ascii = str.maketrans('', '', string.ascii_letters)

    cleaned_str_1 = input_string_1.translate(translation_table_punc)
    print(f"cleaned_str_1 = '{cleaned_str_1}'\n")

    cleaned_str_2 = input_string_2.translate(translation_table_ascii)
    print(f"cleaned_str_2 = '{cleaned_str_2}'\n")

    print('(string cleaning) end::')
    return 0

# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
