#
#
#

import sys
import pandas as pd
import numpy as np


def main():
    print('(stockprice) main:')
    print()

    #
    #
    df = pd.read_csv('timeseries_samples_stock_count-20.csv')

    # print(df)
    # print(df.head(5))

    print()
    print('(stockprice) end::')

    return 0

# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
