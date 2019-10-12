def sum_numbers(f, s):
    return f + s


def subtract(op, t):
    return op - t


def add_and_subtract(f, s, t):
    ops_1 = sum_numbers(f, s)
    res = subtract(ops_1, t)
    return res


first = int(input())
second = int(input())
third = int(input())

print(add_and_subtract(first, second, third))
