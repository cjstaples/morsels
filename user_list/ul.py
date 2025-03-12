#  user list
#  https://www.linkedin.com/pulse/5-python-tricks-you-wish-knew-earlier-benjamin-bennett-alexander-tbzxe/
#

import sys
from collections import UserList

# ---------------

class MyList(UserList):
    def __init__(self, data=None):
        # super().__init__()
        self.data = data if data is not None else []

    def append(self, item):
        if item % 2 == 0:
            self.data.append(item)
        else:
            print("Can't append numbers that are not even")

    # def sort(self, **kwargs):
    def sort(self):
        self.data.sort(reverse = True)


def main():
    print('(user list) main:')
    print()

    obj = MyList([1, 2, 5, 4, 7, 3])
    obj.sort()
    print(f"after sort()    :: {obj = }\n")

    obj.append(11)
    print(f"after append 11 :: {obj = }\n")

    obj.append(20)
    print(f"after append 20 :: {obj = }\n")

    obj.sort()
    print(f"after sort()    :: {obj = }\n")

    print('(user list) end::')
    return 0

# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
