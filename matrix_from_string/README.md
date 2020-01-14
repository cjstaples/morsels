Write a function that accepts a string containing lines of numbers and returns a list of lists of numbers.

=====

For example:
>>> matrix_from_string("3 4 5")
[[3.0, 4.0, 5.0]]
>>> matrix_from_string("3 4 5\n6 7 8")
[[3.0, 4.0, 5.0], [6.0, 7.0, 8.0]]
Make sure your function handles strings with an extra newline at the end:
>>> matrix_from_string("1 2 3\n4 5 6\n7 8 9\n ")
[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]

As a bonus, make sure your function ignores extra whitespace ??:
>>> matrix_from_string("""
...     1   2   3
...
...     4   5   6
...
...     7   8   9
... """)
[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]

=====

Automated tests for this week's exercise can be found here. 

    http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMjYxNDA0NzQxMiIsInVybCI6Imh0dHBzOi8vZ2lzdC5naXRodWIuY29tL3RyZXlodW5uZXIvZjJmYjJiYWVjMTU4YTMxZWMwNWMwZDExOGZiZDcyMWM_X19zPTVzdnZ6eml4aGNhOGtjOTk0bmdtIn0

You'll need to write your function in a module named matrix.py next to the test file. 
To run the tests you'll run "python test_matrix.py" and check the output for "OK". 
You'll see that there are some "expected failures" (or "unexpected successes" maybe). 

If you'd like to do the bonus, you'll want to comment out a line of code in the tests file to test it properly (there's a comment noting which line).

