#
#
#

import sys
import pandas as pd
import numpy as np


def main():
    print('(stockprice) main:')
    print()

    price_low_mark = None
    price_delta_max = None

    #
    #
    df = pd.read_csv('timeseries_samples_stock_count-20.csv')
#    print(df)
    print(df.head(5))

    data = df.to_dict('records')
    for row in data:

        price_current = row['Price']
        print("current price: " + str(price_current))

        if not price_low_mark:
            price_low_mark = price_current

        if not price_delta_max:
            price_delta_max = price_current

        price_low_mark = min(price_current, price_low_mark)
        print("  lowest price today: " + str(price_low_mark))

        price_delta_current = price_current - price_low_mark
        price_delta_max = max(price_delta_current, price_delta_max)
        print("  biggest delta today: " + str(price_delta_max))

    print()
    print('(stockprice) end::')

    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)


def get_max_profit(stock_prices):
    """

    :param stock_prices:
    :return:
    """
    if len(stock_prices) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    # We'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    # Start at the second (index 1) time
    # We can't sell at the first time, since we must buy first,
    # and we can't buy and sell at the same time!
    # If we started at index 0, we'd try to buy *and* sell at time 0.
    # This would give a profit of 0, which is a problem if our
    # max_profit is supposed to be *negative*--we'd return 0.
    for current_time in range(1, len(stock_prices)):
        current_price = stock_prices[current_time]

        # See what our profit would be if we bought at the
        # min price and sold at the current price
        current_potential_profit = current_price - min_price

        # Update max_profit if we can do better
        max_profit = max(max_profit, current_potential_profit)

        # Update min_price so it's always
        # the lowest price we've seen so far
        min_price = min(min_price, current_price)

    return max_profit
