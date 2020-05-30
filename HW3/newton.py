import numpy as np
import matplotlib.pyplot as plt


def Newton(x, f_table):
    n = len(x)

    def P(value):
        sum_formula = f_table[0][0]
        for i in range(1, n):
            def Pro(i):
                production_formula = 1
                for j in range(i):
                    production_formula *= (value - x[j])
                return production_formula

            sum_formula += (Pro(i) * f_table[0][i])
        return sum_formula

    return P


def buildTable(x, f_table):
    n = len(x)
    for i in range(1, n):
        for j in range(n - i):
            # print("*")
            # thanks to geeksforgeeks
            f_table[j][i] = ((f_table[j][i - 1] - f_table[j + 1][i - 1]) /
                             (x[j] - x[i + j]))
    return f_table


def plot(f, my_xs, my_ys):
    x = range(-10, 20)
    y = list(map(f, x))
    x = [w for w in x]
    plt.plot(x, y, linewidth=1.0)
    plt.plot(my_xs, my_ys, 'ro')
    plt.show()


# main
n = int(input("Enter num of inputs: "))
points = []
x = [0] * n
y = [0] * n
f_table = [[0] * (2 * n) for i in range(2 * n)]
for i in range(n):
    x_i, y_i = list(map(float, input().split(", ")))
    x[i] = x_i
    y[i] = y_i
    f_table[i][0] = y_i
    points.append((x_i, y_i))
value = float(input("Enter your value: "))

# ---------
f_table = buildTable(x, f_table)
P = Newton(x, f_table)
print("value: ", value, " P(", value, ")", float(P(value)))

plot(P, x, y)

