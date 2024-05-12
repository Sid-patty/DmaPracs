import pandas as pd
from sklearn.preprocessing import OneHotEncoder
# Read the data from the CSV file
file_path = "exp3_onehot/employee.csv"
df = pd.read_csv(file_path)

# Define the categorical columns
categorical_columns = ['Gender', 'Remarks']

# Initialize OneHotEncoder
encoder = OneHotEncoder()

# Fit and transform the categorical columns
encoded_data = encoder.fit_transform(df[categorical_columns]).toarray()

# Create a DataFrame with the encoded data
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_columns))

# Concatenate the encoded DataFrame with the original DataFrame
final_df = pd.concat([df.drop(categorical_columns, axis=1), encoded_df], axis=1)

# Print the original and encoded dataframes
print("Original DataFrame:")
print(df)
print("\nOne-hot Encoded DataFrame:")
print(final_df)