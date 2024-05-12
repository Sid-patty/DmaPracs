import matplotlib.pyplot as plt
import pandas as pd

# Reading data
data = pd.read_csv('exp6_matplotlib/tips.csv')

# Data
x = data['total_bill']

# Plotting
plt.hist(x, bins=20, color='orange', edgecolor='black', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

# import matplotlib.pyplot as plt

# # Hardcoded input data
# data = [25, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# # Plotting
# plt.hist(data, bins=10, color='orange', edgecolor='black', alpha=0.7)
# plt.title("Histogram")
# plt.xlabel("Total Bill")
# plt.ylabel("Frequency")
# plt.savefig("histogram.png")
# plt.show()
