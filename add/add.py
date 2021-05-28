import sys


def get_max_len(matrix):
    mxl = [len(r) for r in matrix]
    return mxl


def add(*matrix):
    """Add 2D matrixes."""
    combined = []

    matrix_length = get_max_len(matrix[0])
    for m in matrix:
        if get_max_len(m) != matrix_length:
            raise ValueError("matrixes are not equal sizes")

    for rows in zip(*matrix):
        row = []
        for values in zip(*rows):
            row.append(sum(values))
        combined.append(row)
    return combined


if __name__ == '__main__':
    print("exit: add")
    sys.exit(0)
