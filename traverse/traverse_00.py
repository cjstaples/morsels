import os, sys
import math, time


# Traverse directory tree
def traverse(start_path):
    dir_count = 0
    file_count = 0

    for (path, dirs, files) in os.walk(start_path):
        localpath = path.replace(start_path,'')
        print('Directory: {:s}'.format(localpath))
        dir_count += 1

        # Repeat for each file in directory
        for file in files:
            fstat = os.stat(os.path.join(path, file))
            # Print file attributes
            print('\t{:15.15s}'.format(file))
            file_count += 1

    return file_count, dir_count


def main():
    print('(traverse) main:')
    print()

    # Set listing start location
    start_path = "/Users/cstaples/Documents/cashbot/cache"

    file_count, dir_count = traverse(start_path)

    # Print total files and directory count
    print('\nFound {} files in {} directories.'.format(file_count, dir_count))

    print()
    print('(traverse) end::')

    return 0


# ----------------------------------------
if __name__ == '__main__':
    result0 = main()
    sys.exit(0)
