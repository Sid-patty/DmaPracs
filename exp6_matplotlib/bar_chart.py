import matplotlib.pyplot as plt
import pandas as pd

# Reading data
data = pd.read_csv('exp6_matplotlib/tips.csv')

# Data
x = data['day']
y = data['total_bill']

# Plotting
plt.bar(x, y, color='green', edgecolor='blue', linewidth=2)
plt.title("Bar Chart")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.savefig("bar_chart.png")
plt.show()

# import matplotlib.pyplot as plt
# import pandas as pd

# # Hardcoded input data
# data = pd.DataFrame({
#     'day': ['Sun', 'Mon', 'Tue', 'Wed', 'Thu'],
#     'total_bill': [30, 40, 25, 45, 35]
# })

# # Plotting
# plt.bar(data['day'], data['total_bill'], color='green', edgecolor='blue', linewidth=2)
# plt.title("Bar Chart")
# plt.xlabel("Day")
# plt.ylabel("Total Bill")
# plt.savefig("bar_chart.png")
# plt.show()
