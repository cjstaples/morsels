#  flatten list
#  https://www.linkedin.com/pulse/5-python-tricks-you-wish-knew-earlier-benjamin-bennett-alexander-tbzxe/
#

import sys
from more_itertools import collapse

# ---------------

def main():
    print('(flatten list) main:')
    print()

    deeply_nested_list_1 = [[[12, 13], [[14, 15, 16]]]]
    flattened_list_1 = collapse(deeply_nested_list_1)
    print(list(flattened_list_1))

    deeply_nested_list_2 = [[[12, 13], [14, 15, 16], [[14, 15, 16]]]]
    flattened_list_2 = sorted(collapse(deeply_nested_list_2))
    print(str(list(flattened_list_2))+'\n')

    print('(flatten list) end::')
    return 0

# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
