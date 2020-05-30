"""
    Python code for simpson's rule, I used the following source:
    https://www.geeksforgeeks.org/program-simpsons-13-rule/

"""
import numpy


class Config:
    def func(self):
        return numpy.log(self)
        # return self


def calculate_width(ll, ul, n):
    """
     Calculate the width, h = (b-a)/n
    """
    return (ul - ll) / n


def calculate_xi_f_xi(ll, h, n):
    """
    Calculate the values of x0 to xn as x0 = a, x1 = x0 + h, …..xn-1 = xn-2 + h, xn = b.

    Consider y = f(x). Now find the values of y(y0 to yn) for the corresponding x(x0 to xn) values.
    """
    x = list()
    y = list()
    for i in range(n + 1):
        x.append(ll + i * h)
        y.append(Config.func(x[i]))
    return x, y


def simpsons_(ll, ul, n, method="1/3"):
    """
    Substitute all the above found values in the Simpson’s Rule Formula
    to calculate the integral value.

    method could be 1/3, 3/8, custom
    """
    h = calculate_width(ll, ul, n)
    x, fx = calculate_xi_f_xi(ll, h, n)

    res = 0
    if method == "1/3":
        # for n = 2k
        res += fx[0] + fx[n]
        for i in range(1, n):
            if i % 2 != 0:
                res += 4 * fx[i]
            else:
                res += 2 * fx[i]

        res = res * (h / 3)
        return res
    elif method == "3/8":
        # for n = 3k
        res += fx[0] + fx[n]
        for i in range(1, n):
            if i % 3 != 0:
                res += 3 * fx[i]
            else:
                res += 2 * fx[i]

        res = res * (3 * h / 8)
        return res
    elif method == "custom":
        if n % 2 == 0:
            return simpsons_(ll, ul, n, method="1/3")
        elif n % 3 == 0:
            return simpsons_(ll, ul, n, method="3/8")

        # implemented for n=3+ 2k
        # simpson 3/8 rule: x0, x1, x2, x3
        res += fx[0] + 3 * fx[1] + 3*fx[2] + 2*fx[3]
        res *= (3*h / 8)
        # simpson 1/3rule for rest of x
        res_ = 0
        res_ += fx[3] + fx[n]

        for i in range(4, n):
            if (i - 3) % 2 != 0:
                res_ += 4 * fx[i]
            else:
                res_ += 2 * fx[i]

        res_ *= (h / 3)
        res += res_
        return res
    else:
        print("Invalid method!")


if __name__ == '__main__':
    print("%.6f" % simpsons_(10, 12, 2, method="1/3"))
    print("%.6f" % simpsons_(12, 15, 3, method="3/8"))
    print("%.6f" % simpsons_(10, 15, 5, method="custom"))
