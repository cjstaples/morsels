# argdemo.py
# Demonstrates usage of argparse library
import os
import sys
import argparse

# Create program argument parser
arg_parser = argparse.ArgumentParser(prog='argdemo',
                                     usage='%(prog)s [options] path',
                                     description='List the content of a folder',
                                     epilog='VERY exciting stuff...')

# Add the arguments
arg_parser.add_argument('Path',
                        metavar='path',
                        type=str,
                        help='the path to list')

# Execute the parse_args() method
args = arg_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('Path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))
