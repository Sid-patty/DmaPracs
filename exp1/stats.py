import numpy as np
import pandas as pd
from scipy.stats import mode

file_path = "exp1/data.csv"
df = pd.read_csv(file_path)
print(df.columns)

columns = ["Age", "Salary"]

for column in columns:
    data_numeric = df[column].dropna() 

    mean_value = np.mean(data_numeric)
    median_value = np.median(data_numeric)
    mode_value = mode(data_numeric)
    quartiles = np.percentile(data_numeric, [25, 50, 75])
    std_dev = np.std(data_numeric)

    print("\n", column)
    print("Mean : ", mean_value)
    print("Median : ", median_value)
    print("Mode : ", mode_value)
    print("Std_dev : ", std_dev)
    print("First Quartile (Q1):", quartiles[0])
    print("Second Quartile (Q2 or Median):", quartiles[1])
    print("Third Quartile (Q3):", quartiles[2])