import sys


def routes(rows:int, cols:int) -> int:
    if rows == 1 or cols == 1:
        return 1
    return routes(rows-1, cols) + routes(rows, cols-1)


if __name__ == '__main__':

    print(routes(10,10))
    print("exit: memo_misc")
    sys.exit(0)

