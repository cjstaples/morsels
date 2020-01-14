# produce a Fibonacci sequence recursively
import sys

def get_fibonacci_number(n):
   # Fibonacci recursive function
   if n > 1:
       return (get_fibonacci_number(n - 1) + get_fibonacci_number(n - 2))
   else:
       return n


def main():
    print('(Fibonacci) main:')
    print()

    # todo: user input
    #

    # vary non-user input here
    nseq = 20

    # input validation
    if nseq <= 0:
        print("Positive integers only!")
    else:
        print("Sequence follows::")
        for i in range(nseq):
            current_value = get_fibonacci_number(i)
            print(current_value)

    print()
    print('(Fibonacci) end::')

    return 0

# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
