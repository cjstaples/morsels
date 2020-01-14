def tail_0(sequence, n):
    """Return the last n items of given sequence."""
    if n == 0:
        return []
    return list(sequence[-n:])

def tail(iterable, n):
    """Return the last n items of given iterable."""
    items = []
    if n <= 0:
        return []
    for item in iterable:
        items = [*items[-(n-1):], item]
    return items
