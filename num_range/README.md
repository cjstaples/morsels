--
write a function called numeric_range which accepts a list of numbers and returns the difference between the largest and smallest numbers.

Your function should work like this:
 
>>> numeric_range([10, 8, 7, 5, 3, 6, 2])
8
>>> numeric_range([1, 2, 3])
2
>>> numeric_range([4])
0

--
This exercise has a couple optional bonuses.

For the first bonus, I'd like you to make sure your function returns 0 when given an empty list: ✔️

>>> numeric_range([])
0

For the second bonus, I'd like you to make sure your function works with any iterable (not just lists): ✔️

>>> numeric_range({4, 2, 7, 3, 8})
6
>>> numeric_range(n**2 for n in range(10))
81

Try to make sure your solution is relatively memory efficient for very long iterables.
--

Automated tests for this week's exercise can be found here.

    http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMjQ3ODk3MTkzNSIsInVybCI6Imh0dHBzOi8vZ2lzdC5naXRodWIuY29tL3RyZXlodW5uZXIvYzZmZTU2NzljMDI4ZTRlYzRkZDFiNWVmZDgxZDBjOGU_X19zPTVzdnZ6eml4aGNhOGtjOTk0bmdtIn0

You'll need to write your function in a module named numeric_range.py next to the test file.
To run the tests you'll run "python test_numeric_range.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe).
If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.

===
original content from python morsels:
Trey Hunner trey@truthful.technology via dripemail2.com
