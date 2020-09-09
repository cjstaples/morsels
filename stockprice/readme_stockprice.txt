Question
    Given a set of stock prices across one day, what is the maximum profit a trader could have made with one purchase and sale of one share?
    Write a function that takes a time series array of 330 stock prices, one per minute from 9:30a.m. to 4p.m., and returns the maximum possible profit (sale price - purchase price) from buying and selling one share once. The sale must come after the purchase.
    * There are actually 390 data points... :)

Suggestions
    Allow the candidate to explore the problem and write a brute force approach initially if they find it helpful.

Some questions to ask:
    What if the price goes down all day?
    How does this solution perform as we give it longer input arrays?
    Could this be done in linear time, looping through the list only once?

ref:
    https://towardsdatascience.com/basic-time-series-manipulation-with-pandas-4432afee64ea

