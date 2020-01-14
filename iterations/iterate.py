#   iterate over all the things
#
#   making a class iterable - do these things:
#       - respond to iter
#       - respond to next
#       - throw StopIteration when we're out of stuff to iterate over
#

import sys

class Itsa(object):
    def __init__(self, data):
        print("Now in Itsa.__init__")
        self.data = data
        self.index = 0
    def __iter__(self):
        print("Now in Itsa.__iter__")
        return self
    def __next__(self):
        print("Now in Itsa.__next__")
        if self.index >= len(self.data):
            print("End of iterations")
            raise(StopIteration)
        value = self.data[self.index]
        self.index += 1
        return value

class Itsb(object):
    def __init__(self, data):
        print("Now in Itsb.__init__")
        self.data = data
        self.index = len(data) - 1
    def __iter__(self):
        print("Now in Itsb.__iter__")
        return self
    def __next__(self):
        print("Now in Itsb.__next__")
        if self.index < 0:
            print("End of iterations")
            raise(StopIteration)
        value = self.data[self.index]
        self.index -= 1
        return value


def main():
    print('(iterate) main:')
    print()

    for item in Itsa('abcd'):
        print(item)

    print()
    print('(iterate) mid::')
    print()

    for item in Itsb('efgh'):
        print(item)

    print()
    print('(iterate) end::')

    return 0

# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
