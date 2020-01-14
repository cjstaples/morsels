# produce a Fibonacci sequence recursively
import sys
import camelot

def get_data():
    return

def main():
    print('(pdf_check) main:')
    print()

    # todo: user input
    #
    tables = camelot.read_pdf('foo.pdf')

    print(tables[0].to_csv('foo.csv'))

    print()
    print('(pdf_check) end::')

    return 0

# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)

#
#   https://blog.socialcops.com/technology/engineering/camelot-python-library-pdf-data/
#
# >>> import camelot
# >>> tables = camelot.read_pdf('foo.pdf')
# >>> tables
# <TableList n=1>
# >>> tables.export('foo.csv', f='csv', compress=True) # json, excel, html
# >>> tables[0]
# <Table shape=(7, 7)>
# >>> tables[0].parsing_report
# {
#     'accuracy': 99.02,
#     'whitespace': 12.24,
#     'order': 1,
#     'page': 1
# }
# >>> tables[0].to_csv('foo.csv') # to_json, to_excel, to_html
# >>> tables[0].df # get a pandas DataFrame!
