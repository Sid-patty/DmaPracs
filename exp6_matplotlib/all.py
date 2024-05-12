import matplotlib.pyplot as plt
import pandas as pd

# Hardcoded input data for each visualization
line_x = [10, 20, 30, 40]
line_y = [20, 25, 35, 55]

bar_data = pd.DataFrame({
    'day': ['Sun', 'Mon', 'Tue', 'Wed', 'Thu'],
    'total_bill': [30, 40, 25, 45, 35]
})

hist_data = [25, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

scatter_x = [25, 30, 35, 40, 45, 50]
scatter_y = [10, 20, 30, 40, 50, 60]

pie_labels = ['A', 'B', 'C', 'D']
pie_data = [25, 30, 20, 25]

# Line Chart
plt.figure(figsize=(8, 6))
plt.plot(line_x, line_y, color='blue', linewidth=2,
         marker='o', markersize=8, linestyle='--')
plt.title("Line Chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.savefig("line_chart.png")
plt.show()

# Bar Chart
plt.figure(figsize=(8, 6))
plt.bar(bar_data['day'], bar_data['total_bill'],
        color='green', edgecolor='blue', linewidth=2)
plt.title("Bar Chart")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.savefig("bar_chart.png")
plt.show()

# Histogram
plt.figure(figsize=(8, 6))
plt.hist(hist_data, bins=10, color='orange', edgecolor='black', alpha=0.7)
plt.title("Histogram")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

# Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(scatter_x, scatter_y, color='red', marker='o', s=50, alpha=0.5)
plt.title("Scatter Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.savefig("scatter_plot.png")
plt.show()

# Pie Chart
plt.figure(figsize=(8, 6))
plt.pie(pie_data, labels=pie_labels, autopct='%1.1f%%', startangle=140,
        colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'])
plt.title("Pie Chart")
plt.savefig("pie_chart.png")
plt.show()