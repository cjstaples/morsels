import collections
import os
import sys
import time


def numeric_range(iterable_input):

    numbers = list(iterable_input)
    if not numbers:
        return 0
    else:
        return max(numbers) - min(numbers)


if __name__ == '__main__':
    #
    #

    # print(num_range([2, 3, 4]))

    print("exit: num_range")
    sys.exit(0)


