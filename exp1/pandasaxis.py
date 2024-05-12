import pandas as pd

# Load data from CSV file using pandas
df = pd.read_csv('exp1/data2.csv')

# Axis=0
mean_axis_0 = df.mean(axis=0)
median_axis_0 = df.median(axis=0)
mode_axis_0 = df.mode(axis=0).iloc[0]
std_deviation_axis_0 = df.std(axis=0)

print("Mean along axis=0:\n", mean_axis_0)
print("\nMedian along axis=0:\n", median_axis_0)
print("\nMode along axis=0:\n", mode_axis_0)
print("\nStandard Deviation along axis=0:\n", std_deviation_axis_0)

# Axis=1
mean_axis_1 = df.mean(axis=1)
median_axis_1 = df.median(axis=1)
mode_axis_1 = df.mode(axis=1).iloc[0]
std_deviation_axis_1 = df.std(axis=1)

print("\nMean along axis=1:\n", mean_axis_1)
print("\nMedian along axis=1:\n", median_axis_1)
print("\nMode along axis=1:\n", mode_axis_1)
print("\nStandard Deviation along axis=1:\n", std_deviation_axis_1)
