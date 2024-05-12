import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Define the dataset
dataset = [
    ['Bread', 'Butter', 'Milk'],
    ['Bread', 'Butter'],
    ['Beer', 'Cookies', 'Diapers'],
    ['Milk', 'Diapers', 'Bread', 'Butter'],
    ['Beer', 'Diapers']
]

# Initialize TransactionEncoder and transform the dataset
te = TransactionEncoder()
te_ary = te.fit_transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Find frequent itemsets with minimum support of 0.4
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

# Generate association rules with minimum confidence of 0.7
res = association_rules(
    frequent_itemsets, metric='confidence', min_threshold=0.7)

# Select relevant columns from the association rules DataFrame
res1 = res[['antecedents', 'consequents', 'support', 'confidence', 'lift']]

# Filter rules with confidence greater than or equal to 1
res2 = res1[res1['confidence'] >= 1]

# Print the filtered association rules
print(res2)