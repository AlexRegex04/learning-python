# SciPy Optimizers
from scipy.optimize import root, minimize
from math import cos


def eqn(x):
    return x + 10


myroot = root(eqn, 0)


def eqn(x):
    return x**2 + x + 2


mymin = minimize(eqn, 0, method='BFGS')

print(mymin)