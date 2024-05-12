import matplotlib.pyplot as plt

# Data
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

# Plotting
plt.plot(x, y, color='blue', linewidth=2,
         marker='o', markersize=8, linestyle='--')
plt.title("Line Chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.savefig("line_chart.png")
plt.show()