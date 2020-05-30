def euler_method(y_prime_fun, x_initial, y_initial, h, x_goal):
    N = int((x_goal - x_initial) / h)
    x = []
    for i in range(N):
        x.append(round((x_initial + i * h), 4))

    y = [y_initial]
    for i in range(N):
        y.append(round((y[-1] + h * y_prime_fun(x[i], y[-1])), 4))
    return y[-1]


if __name__ == '__main__':
    print("Part A:")
    print("Goal point is two: ")
    # Calculate Y(2):
    print(euler_method(lambda x,y: 2*y, 0, 3, 0.1, 2))

    print("\n\nPart B:")
    fun_ = input("Y' =  (example: 2*y + x) \t")
    y_prime_fun = (lambda x, y: eval(fun_))
    x_initial = float(input("x0 = \t"))
    y_initial = float(input("Y(x0) = \t"))
    h = float(input("h: \t"))
    x_goal = float(input("Y(x_goal) = ?? -> x_goal = \t"))
