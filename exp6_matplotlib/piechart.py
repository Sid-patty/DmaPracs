import matplotlib.pyplot as plt

# Data
cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR']
data = [23, 13, 35, 15, 12]
explode = (0.1, 0, 0, 0, 0)
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen']

# Plotting
plt.pie(data, explode=explode, labels=cars, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Pie Chart")
plt.savefig("pie_chart.png")
plt.show()

# import matplotlib.pyplot as plt

# # Hardcoded input data
# labels = ['A', 'B', 'C', 'D']
# sizes = [25, 30, 20, 25]

# # Plotting
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['gold', 'yellowgreen', 'lightcoral', 'lightskyblue'])
# plt.title("Pie Chart")
# plt.savefig("pie_chart.png")
# plt.show()
