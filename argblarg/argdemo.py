# argdemo.py
# Demonstrates usage of arg
import sys


def sum_args(*args):
    res_s = 0
    # Iterate over args
    for a in args:
        res_s += a
    return res_s


def concat_kw(**kwargs):
    accum = ""
    # Iterate over kwargs
    for arg in kwargs.values():
        accum += arg
    return accum


def main():
    print('(argdemo) main:')
    print()

    result1 = concat_kw(a="aaa", b="bbb", c="ccc")
    print('result1: ', result1)

    result2 = sum_args(1, 2, 3)
    print('result2: ', result2)

    print()
    print('(argdemo) end::')

    return 0


# ----------------------------------------
if __name__ == '__main__':
    result0 = main()
    sys.exit(0)
