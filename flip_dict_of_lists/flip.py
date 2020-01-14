import collections
import os
import sys
import time
from collections import defaultdict


def flip_dict_of_lists(dict_of_lists):
    """Return a "flipped" dictionary of lists."""
    flipped = {}
    for key, values in dict_of_lists.items():
        for value in values:
            if value not in flipped:
                flipped[value] = []
            flipped[value].append(key)
    return flipped


if __name__ == '__main__':

    m = {
            'Alice': ['McDonalds', 'Wendys'],
            'Bobbie': ['Wendys', 'Burger King'],
            'Carl': ['Burger King', 'Wendys', 'McDonalds'],
            'Dave': ['McDonalds', 'Arbys'],
    }

    output_values = flip_dict_of_lists(m)
    print('\n',output_values,'\n')
    print("exit: flip")
    sys.exit(0)

