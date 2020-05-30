# inputs = [function: string, a: float, b: float, N: int]
inputs = ['x**3 + 5', -10.5, 11, 10]
f = lambda x: eval(inputs[0])
a = float(inputs[1])
b = float(inputs[2])
N = int(inputs[3])


def next_x(f, current_a, current_b):
    return current_a - f(current_a) * (current_b - current_a) / (f(current_b) - f(current_a))


def secant(f, a, b, N):
    if f(a) * f(b) >= 0:
        print("secant method failed!!!")
        return
    current_a = a
    current_b = b
    for i in range(0, N):
        current_x = next_x(f, current_a, current_b)
        # print(current_x)
        f_current_x = f(current_x)
        if f_current_x == 0:
            # found exact answer
            print("exact point is: ", current_x)
            return current_x
        elif f(current_a) * f_current_x < 0:
            #     (a, x)
            current_b = current_x
        elif f(current_b) * f_current_x < 0:
            #     (x, b)
            current_a = current_x
        else:
            print("secant method failed!!!")
            return

    estimation = next_x(f, current_a, current_b)
    print("estimation is: ", estimation)
    return


secant(f, a, b, N)

