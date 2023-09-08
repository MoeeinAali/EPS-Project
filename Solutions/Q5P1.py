import random


def monte_carlo_integral(f, a, b, c, n):
    points_under_curve = 0
    for i in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, c)
        if y <= f(x):
            points_under_curve += 1

    integral_approximation = c * (b - a) * (points_under_curve / n)
    return integral_approximation


def f(x):
    return x


a = 0
b = 5
c = 5
n = 1000000
approximation = monte_carlo_integral(f, a, b, c, n)
print("f(x) = x integral approximation: ", approximation)
