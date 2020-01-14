# produce a Fibonacci sequence recursively
import sys

def brand_code_for_prefix(prefix, site='semiprod'):
    # BY_PREFIX = SiteBrands.for_site(site).by_prefix
    # brand = BY_PREFIX.get(prefix)

    brand = ''

    code = brand and brand.code
    return code

def main():
    print('(brand) main:')
    print()

    # todo: user input
    #
    prefix = 'xxx'
    net_code = brand_code_for_prefix(prefix,'qa')

    print()
    print('(brand) end::')

    return 0

# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
