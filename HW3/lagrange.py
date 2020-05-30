import matplotlib.pyplot as plt

def plot(f,years, rates):
    x = range(-10, 50)
    y = list(map(f, x))
    x = [w+1950 for w in x ]
    plt.plot(x, y, linewidth=1.0)
    plt.plot(years, rates, 'ro')
    plt.show()

def lagrange(points):
    n = len(points)
    def P(x):
        p_formula = 0
        for i in range(n):
            xi, fi = points[i]
            def L(i, n):
                l_formula_i = 1
                for j in range(n):
                    if i == j:
                        continue
                    xj, yj = points[j]
                    l_formula_i *= (x - xj) / float(xi - xj)
                return l_formula_i
            p_formula += fi * L(i, n)
        return p_formula

    return P


years = [1995, 1990, 1985, 1980, 1975, 1970, 1965, 1960, 1955, 1950]
rate = [0.85, 1.52, 1.73, 1.42, 1.82, 2.54, 2.37, 1.58, 1.44, 2.7]
points = []
for i in range(len(years)):
    points.append((years[i] - 1950, rate[i]))
P = lagrange(points)
print(P(1957-1950))
print(P(1987-1957))
print(P)
plot(P,years, rate)

