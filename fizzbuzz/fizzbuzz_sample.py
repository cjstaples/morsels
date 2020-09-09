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
    cases = range(1, 101)

    for case in cases:

        case_output = fizzbuzz_logic(case)
        print(case_output)

    print()
    print('(fizzbuzz) end::')

    return 0


def fizzbuzz_logic(case):
    output = ''

    # simplistic, but handle both true without dealing with multi line issue
    if check_fizz(case) & check_buzz(case):
        output = 'FizzBuzz'
    # only fizz true
    elif check_fizz(case):
        output = 'Fizz'
    # only buzz true
    elif check_buzz(case):
        output = 'Buzz'
    # neither true
    else:
        output = case

    return output


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
