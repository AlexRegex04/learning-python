from math import *
['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', '', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', '', '', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot',
    'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', '', '', 'prod', 'radians', 'remainder', 'sin', 'sinh', '', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

print(ceil(10.4))
print(floor(10.8))
print(sqrt(9))
print(pi)
#* Calculating the Power of a Number
print(pow(2, 2))
print(factorial(4))
print(radians(180))
print(cos(radians(60)))
print(sin(radians(30)))
print(tau)
print(gamma(4))
print(isfinite(5345))
# Infinity

print(inf*10)
print(-inf)
print(inf > 10e109)
print(-inf < -10e109)
try:
    print("The factorial of 6.5 in: ", factorial(6.5))
except Exception:
    print("Cannot calculate factorial of a non-integral number")

# * Calculating the Absolute Value
x = -45
print("The absolute value of -45 is: ", fabs(x))

# *Calculating the Exponential
num1 = 6
num2 = -3
num3 = 0.00
# passing above values to the exp() function
print(f"The exponenetial value of {num1} is: ", exp(num1))
print(f"The exponenetial value of {num2} is: ", exp(num2))
print(f"The exponenetial value of {num3} is: ", exp(num3))

print(fmod(10,3))
print(modf(10.5345))
print(expm1(6))
print(log(16,4))