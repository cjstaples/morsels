#  set list
#  https://www.linkedin.com/pulse/5-python-tricks-you-wish-knew-earlier-benjamin-bennett-alexander-tbzxe/
#

import sys

# ---------------
#   set() function creates a set from a list, removing duplicate elements
def check_list(lst: list):
    # if len(set(lst)) == 1:
    if len(set(lst)) in [0, 1]:
        return "List items identical"
    else:
        return "List items not identical"


def main():
    print('(set list) main:')
    print()

    list_check_1 = [2, 3, 4, 5, 7, 5]
    print(check_list(list_check_1))

    list_check_2 = [2, 2, 2, 2]
    print(check_list(list_check_2))

    list_check_3 = [2, 3, 4, 5]
    print(check_list(list_check_3))

    list_check_4 = [7]
    print(check_list(list_check_4))

    list_check_5 = []
    print(check_list(list_check_5))

    print('(set list) end::')
    return 0

# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
