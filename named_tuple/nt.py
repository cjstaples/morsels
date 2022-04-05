#  named tuple sample
#
#

import sys
from collections import namedtuple


def main():
    print('(named tuple) main:')
    print()

    # todo: user input
    #

    Person = namedtuple("Person", "name children")
    john = Person("john doe", ["Timmy", "Jimmy"])

    print(f":::::::::::::::::::::::::::::::::::")
    print(f"::: {john.name}")
    print(f"::: {john.children}")
    for item in john.children:
        print(f"xxx {item}")

    Devdata = namedtuple("Devdata", "app_name category country is_current os_name os_version push_enabled")
    dev1 = Devdata("Chrome", "PERSONAL_COMPUTER", "United States", False, "OSX", "10", False)
    dev2 = Devdata("Chrome", "PERSONAL_COMPUTER", "United States", False, "OSX", "10", False)
    dev3 = Devdata("Chrome", "PERSONAL_COMPUTER", "United States", False, "OSX", "11", False)

    print(f":::::::::::::::::::::::::::::::::::")
    print(f"::: {dev1.app_name}")
    print(f"::: {dev1.os_version}")
    print(f"::: {dev1.country}")
    print(f"::: {dev3.app_name}")
    print(f"::: {dev3.os_version}")
    print(f"::: {dev3.country}")

    print(f":::::::::::::::::::::::::::::::::::")
    for item in [dev1, dev2, dev3]:
        print(f"::: {item.app_name}")
        print(f"::: {item.os_version}")
        print(f"::: {item.country}")
        print(f"--- ---------------------------")

    print()
    print('(named tuple) end::')

    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
