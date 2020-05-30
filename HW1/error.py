# getting input
x = float(input("Please, enter an input to compute natural logarithm:   "))
# limiting decimal points
x = float("{0:.4f}".format(x))


def ln(x, n):
    result = 0
    for i in range(1, n, 1):
        result += (((x - 1) / (x + 1)) ** (2 * i - 1)) / (2 * i - 1)
    #     thanks to http://math2.org/math/expansion/log.htm for taylor series
    #     enough to calculate to 5 decimal points!

    result = float("{0:.4f}".format(2 * result))
    return result


def find_optimal_n(x):
    n = 1
    while (((x - 1) / (x + 1)) ** (2 * n - 1)) / (2 * n - 1) > 0.000025:
        n += 1
    return n


result = ln(x, find_optimal_n(x))
print(result)
# test time!
from math import log

# 2.7 as input
assert log(2.7) - 0.0001 < ln(2.7, find_optimal_n(2.7))
assert log(2.7) + 0.0001 > ln(2.7, find_optimal_n(2.7))

