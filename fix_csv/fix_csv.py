import argparse
import csv
import sys


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_input')
    parser.add_argument('file_output')
    parser.add_argument('--in-delimiter', dest='delim')
    parser.add_argument('--in-quote', dest='quote')
    arglist = parser.parse_args()
    return arglist


def get_input(file):
    with open(file, newline='') as infile:
        arguments = {}
        if args.delim:
            arguments['delimiter'] = args.delim
        if args.quote:
            arguments['quotechar'] = args.quote
        if not (args.delim or args.quote):
            arguments['dialect'] = csv.Sniffer().sniff(infile.read())
            infile.seek(0)

        reader = csv.reader(infile, **arguments)
        rows = list(reader)
    return rows


def write_output(file, rows):
    with open(file, mode='wt', newline='') as outfile:
        csv.writer(outfile).writerows(rows)
    outfile.close()
    return


if __name__ == '__main__':

    args = parse_args()

    file_input = args.file_input
    file_output = args.file_output

    input_rows = get_input(file_input)
    write_output(file_output, input_rows)

    sys.exit(0)
