import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load data
data = pd.read_csv("exp4_datatransform/50_Startups.csv")

# Data Transformation: Standardize the variable
#scaler = StandardScaler()
#data[['R&D Spend', 'Marketing Spend']] = scaler.fit_transform(
 #   data[['R&D Spend', 'Marketing Spend']])

# Data Modeling: Partition the dataset
X = data[['R&D Spend', 'Marketing Spend']]
y = data['Profit']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0)

print("X Train \n", X_train)
print("X Test \n", X_test)
print("Y Train \n", y_train)
print("Y Test \n", y_test)

train_count = len(X_train)
test_count = len(X_test)

# Visualization
plt.figure(figsize=(8, 6))
plt.bar('Train', train_count, width=0.4, color='blue', label='Train Data')
plt.bar('Test', test_count, width=0.4, label='Test Data', color='red')
plt.xlabel('Data Set')
plt.ylabel('Number of Samples')
plt.title('Number of Samples in Train and Test Sets')
plt.text('Train', train_count, str(train_count), ha='center', va='bottom')
plt.text('Test', test_count, str(test_count), ha='center', va='bottom')
plt.legend()
plt.show()