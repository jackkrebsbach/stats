import numpy as np
from scipy import stats

# Create a sample array
array = np.array([1, 2, 3, 4, 5])
second_array = np.array([1,2,3,5])


# Perform a simple calculation
result = array + 10

# Print the result
print("Original array:", array)
print("Array after adding 10:", result)

# Generate sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

# Print the results
print("Slope:", slope)
print("Intercept:", intercept)
print("R-squared:", r_value**2)
print("P-value:", p_value)
print("hello world")
