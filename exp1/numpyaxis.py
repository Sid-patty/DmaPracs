import numpy as np
from scipy.stats import mode

# Load data from CSV file
data = np.genfromtxt('exp1/data2.csv', delimiter=',', skip_header=1)

# Axis=0
mean_axis_0 = np.mean(data, axis=0)
median_axis_0 = np.median(data, axis=0)
mode_axis_0, mode_count_axis_0 = mode(data, axis=0)
std_deviation_axis_0 = np.std(data, axis=0)

print("Mean along axis=0:", mean_axis_0)
print("Median along axis=0:", median_axis_0)
print("Mode along axis=0:", mode_axis_0, "(count:", mode_count_axis_0[0], ")")
print("Standard Deviation along axis=0:", std_deviation_axis_0)

# Axis=1
mean_axis_1 = np.mean(data, axis=1)
median_axis_1 = np.median(data, axis=1)
mode_axis_1, mode_count_axis_1 = mode(data, axis=1)
std_deviation_axis_1 = np.std(data, axis=1)

print("\nMean along axis=1:", mean_axis_1)
print("Median along axis=1:", median_axis_1)
print("Mode along axis=1:", mode_axis_1, "(count:", mode_count_axis_1[0], ")")
print("Standard Deviation along axis=1:", std_deviation_axis_1)