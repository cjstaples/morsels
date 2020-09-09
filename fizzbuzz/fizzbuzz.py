#  fizzbuzz sample
#  pretty standard interview stuff
#  e.g.
#  https://wiki.c2.com/?FizzBuzzTest
#

import sys


def main():
    print('(fizzbuzz) main:')
    print()

    # todo: any user input
    #
    cases = range(1,101)

    for case in cases:
        # simplistic, but handle both true without dealing with multi line issue
        if check_fizz(case) & check_buzz(case):
            print('FizzBuzz')
        # only fizz true
        elif check_fizz(case):
            print('Fizz')
        # only buzz true
        elif check_buzz(case):
            print('Buzz')
        # neither true
        else:
            print(case)

    print()
    print('(fizzbuzz) end::')

    return 0

def check_buzz(case):
    check = False
    if (case % 5) == 0:
        check = True
    return check

def check_fizz(case):
    check = False
    if (case % 3) == 0:
        check = True
    return check


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
