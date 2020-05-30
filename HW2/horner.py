# n = 5
# a = [1, -6, 8, 8, 4, -40]
# x = 3
n = int(input("Please enter what is degree of polynomial function:\t‌"))
a = [0.0] * (n + 1)
for i in range(n, -1, -1):
    a[i] = float(input("Enter coefficient of X ^ " + str(i) + " :\t"))
x = float(input("Please enter x value:\t"))

b = [0.0] * (n + 1)
b[n] = a[n]
for i in range(n - 1, -1, -1):
    b[i] = b[i + 1] * x + a[i]
print("P(" + str(x) + ") = " + str(b[0]))

