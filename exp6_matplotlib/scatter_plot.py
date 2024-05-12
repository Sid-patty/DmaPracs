import matplotlib.pyplot as plt
import pandas as pd

# Reading data
data = pd.read_csv('exp6_matplotlib/tips.csv')

# Data
x = data['total_bill']
y = data['day']

# Plotting
plt.scatter(x, y, color='red', marker='o', s=50, alpha=0.5)
plt.title("Scatter Plot")
plt.xlabel("Total Bill")
plt.ylabel("Day")
plt.savefig("scatter_plot.png")
plt.show()

# import matplotlib.pyplot as plt

# # Hardcoded input data
# x = [25, 30, 35, 40, 45, 50]
# y = [10, 20, 30, 40, 50, 60]

# # Plotting
# plt.scatter(x, y, color='red', marker='o', s=50, alpha=0.5)
# plt.title("Scatter Plot")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.savefig("scatter_plot.png")
# plt.show()
