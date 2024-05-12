import pandas as pd

# Load the data from the CSV file
filename = 'exp2_null/data.csv'
df = pd.read_csv(filename)

# Identify missing values
null_values = df.isnull()

# Fill missing values with zero
df_filled_with_zero = df.fillna(0)

# Remove rows with missing values
df_dropna = df.dropna()

# Print results
print("Original DataFrame:\n", df)
print("\nNull values check:\n", null_values)
print("\nDataFrame with missing values replaced by 0:\n", df_filled_with_zero)
print("\nDataFrame after dropping rows with missing values:\n", df_dropna)

# Assessing impact on data quality
num_rows_original = df.shape[0]
num_rows_dropna = df_dropna.shape[0]
num_rows_filled_with_zero = df_filled_with_zero.shape[0]

print("\nNumber of rows in original DataFrame:", num_rows_original)
print("Number of rows after dropping rows with missing values:", num_rows_dropna)
print("Number of rows after filling missing values with zero:",
      num_rows_filled_with_zero)