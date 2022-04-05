#  named dict sample
#
#

import sys


def main():
    print('(named dict) main:')
    print()

    print(f":::::::::::::::::::::::::::::::::::")

    dev0 = {
        "app_name": "Chrome",
        "category": "PERSONAL_COMPUTER",
        "country": "United States",
        "is_current": False,
        "os_name": "",
        "os_version": "00",
        "push_enabled": False,
    }
    dev1 = {
        "app_name": "Chrome",
        "category": "PERSONAL_COMPUTER",
        "country": "United States",
        "is_current": False,
        "os_name": "",
        "os_version": "11",
        "push_enabled": False,
    }
    dev2 = {
        "app_name": "Chrome",
        "category": "PERSONAL_COMPUTER",
        "country": "United States",
        "is_current": False,
        "os_name": "",
        "os_version": "22",
        "push_enabled": False,
    }

    print(f":::::::::::::::::::::::::::::::::::")
    print(f"::: {dev0['app_name']}")
    print(f"::: {dev0['country']}")
    print(f"::: {dev0['os_version']}")

    print(f":::::::::::::::::::::::::::::::::::")
    for item in [dev0, dev1, dev2]:
        print(f"::: {item}")
        print(f"--- ---------------------------")

    print()
    print('(named dict) end::')

    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
