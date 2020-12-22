def sum_numbers(numbers=None):
    if numbers is None:
        numbers = list(range(1, 101))

    listsum = 0
    for x in numbers:
        listsum += x
    return listsum


if __name__ == '__main__':
    result = sum_numbers()
    print(result)