import numpy as np

# Define the sum function
def infinite_series(x, epsilon=0.001):
    sum_result = 0
    k = 0
    while True:
        term = x / (2*k + 1)**3 * np.sin(2*k + 1)
        sum_result += term
        if abs(term) < epsilon:
            break
        k += 1
    return sum_result

# Define the range and step
a = -1
b = 1
h = 0.1

# Create the tabulation
x_values = np.arange(a, b + h, h)
for x in x_values:
    result = infinite_series(x, epsilon=0.001)
    print(f"x = {x:.2f}, sum = {result:.5f}")