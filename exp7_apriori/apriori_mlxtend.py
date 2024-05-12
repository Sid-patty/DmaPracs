from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

# Given dataset
dataset = [
    ["1", "3", "4"],
    ["2", "3", "5"],
    ["1", "2", "3", "5"],
    ["2", "5"]
]

# Initialize TransactionEncoder
te = TransactionEncoder()
# Transform the dataset into a transaction array format
te_ary = te.fit(dataset).transform(dataset)
# Convert the transaction array into a DataFrame
df = pd.DataFrame(te_ary, columns=te.columns_)

# Get frequent itemsets
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

# Print frequent itemsets
print("Frequent itemsets:")
print(frequent_itemsets)

# Generate association rules
association_rules_df = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# Print association rules
print("\nAssociation rules:")
print(association_rules_df)

# Print final association rules with support, confidence, and lift
print("\nFinal association rules:")
print(association_rules_df[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
