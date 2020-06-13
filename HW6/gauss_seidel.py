import math
import numpy as np


def get_input():
    """
    example: 1, 2, 3, 4, 5, 6, 7, 8
    :return: A: [[1, 2], [3, 4]]
    :return: b: [5, 6]
    :return: initial: [7, 8]
    """
    nums = list(map(float, input().split(", ")))
    n = int(math.sqrt(len(nums)))
    b = nums[n * n: n * n + n]
    intial = nums[n * n + n:]
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = nums[i * n + j]

    return A, b, intial


def sorted_matrix(A, b, n):
    """
    this function helps to reduce error by ordering rows pf matrix
    """
    c = [0] * n
    for i in range(n):
        c[i] = A[i][0]
    c_arg_sort = np.argsort(c)
    c_arg_sort = c_arg_sort[::-1]

    A_prime = [[0] * n for _ in range(n)]
    b_prime = [0] * n
    for i in range(n):
        A_prime[i] = A[c_arg_sort[i]]
        b_prime[i] = b[c_arg_sort[i]]

    return A_prime, b_prime


def find_next_iter(initial_guess, A, b, n):
    """
    using this method to calculate next X vector based on current X
    """
    X = initial_guess
    for i in range(n):
        X[i] = b[i]
        for j in range(0, n):
            if j != i:
                X[i] -= round(A[i][j] * X[j], 4)
        X[i] = round(X[i] / A[i][i], 4)
    return X


def gauss_seidel(initial_guess, A, b, n):
    """
    this method  iterates 3 times to get to result
    """
    X = initial_guess
    for i in range(3):
        X = find_next_iter(X, A, b, n)
    return X


# gauss_seidel([1, 2, 5], [[144, 12, 1], [64, 8, 1], [25, 5, 1]], [279.2, 177.2, 106.8], 3)

if __name__ == '__main__':
    """
    example: 144, 12, 1, 64, 8, 1, 25, 5, 1, 279.2, 177.2, 106.8, 1, 1, 1
    """
    A, b, initial_guess = get_input()
    print(A)
    print(b)
    print(initial_guess)
    n = len(b)
    A, b = sorted_matrix(A, b, n)

    result = gauss_seidel(initial_guess, A, b, n)
    print(result)
