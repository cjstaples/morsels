#  filterfalse
#  https://www.linkedin.com/pulse/5-python-tricks-you-wish-knew-earlier-benjamin-bennett-alexander-tbzxe/
#

import sys
from itertools import filterfalse

def is_odd(x):
    return x % 2 != 0

filter_list_1 = [1, 2, 3, 4, 5, 6]
filter_list_2 = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# ---------------

def main():
    print('(filterfalse) main:')
    print()

    print(f'{filter_list_1 = }\n')
    filtered_list = list(filterfalse(is_odd, filter_list_1))
    print(f'{filtered_list = }\n')

    print(f'{filter_list_2 = }\n')
    filtered_list = list(filterfalse(is_odd, filter_list_2))
    print(f'{filtered_list = }\n')

    print('(filterfalse) end::')

    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
