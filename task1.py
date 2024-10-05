import numpy as np
import math

def sec(x):
    return 1 / np.cos(x)

def log_base_10_e():
    return np.log10(np.e)

a = 4
b = 7
h = 0.2

x_values =np.arange(a, b + h, h)
for x in x_values:
    if x < 4.5:
        result = sec(x * np.cos(x))
    elif 4.5 <= x < 6:
        result = x**3 + 4
    else:
        result = x * log_base_10_e()

    print(f"x = {x:.2f}, f(x) = {result:.5f}")

