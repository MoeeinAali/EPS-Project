import random
import math


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
    if abs(x) > 1:
        return 0
    else:
        e = math.e
        return pow(e, x * x)


def g(x):
    pi = math.pi
    if x > 0 and x < pi:
        return math.sin(x) / x
    else:
        return 0


a = 0
b = 5
c = 5
n = 1000000
approximation1 = monte_carlo_integral(f, a, b, c, n)
approximation2 = monte_carlo_integral(g, a, b, c, n)
print("f(x) integral approximation: ", approximation1)
print("g(x) integral approximation: ", approximation2)