from itertools import combinations
from collections import defaultdict

min_support = 2
min_confidence = 70

# table = {
#     "T1": [1, 2, 4],
#     "T2": [1, 2, 5],
#     "T3": [1, 3, 5],
#     "T4": [2, 4],
#     "T5": [2, 3],
#     "T6": [1, 2, 3, 5],
#     "T7": [1, 3],
#     "T8": [1, 2, 3],
#     "T9": [2, 3],
#     "T10": [3, 5]
# }

table = {
    "T1": [1, 3, 4],
    "T2": [2, 3, 5],
    "T3": [1, 2, 3, 5],
    "T4": [2, 5]
}

length = len(table)


def mainOperation(data):
    data = sorted(data.items(), key=lambda item: item[1], reverse=True)
    data = dict(data)
    keys = []
    for key, value in data.items():
        if value < min_support:
            keys.append(key)
    for key in keys:
        del data[key]
    return data


# Counting support for individual items
dict1 = {i: 0 for i in range(1, 6)}
for values in table.values():
    for value in values:
        dict1[value] += 1
dict1 = mainOperation(dict1)

# Print frequent itemsets with frequency and compare with support
print("Frequent 1-itemsets:")
for item, support in dict1.items():
    print(f"{(item,)} : {support} (Support: {support >= min_support})")

# Counting support for pairs
combos = list(combinations(dict1.keys(), 2))
dict2 = defaultdict(int)
for combo in combos:
    for value in table.values():
        if set(combo).issubset(set(value)):
            dict2[combo] += 1
dict2 = mainOperation(dict2)

# Print frequent itemsets with frequency and compare with support
print("\nFrequent 2-itemsets:")
for itemset, support in dict2.items():
    print(f"{itemset} : {support} (Support: {support >= min_support})")

# Counting support for triples
combos = list(combinations(dict1.keys(), 3))
dict3 = defaultdict(int)
for combo in combos:
    for value in table.values():
        if set(combo).issubset(set(value)):
            dict3[combo] += 1
dict3 = mainOperation(dict3)

# Print frequent itemsets with frequency and compare with support
print("\nFrequent 3-itemsets:")
for itemset, support in dict3.items():
    print(f"{itemset} : {support} (Support: {support >= min_support})")

# Merging dictionaries
dict1.update(dict2)
dict1.update(dict3)
main_dict = dict1

finalList = list(dict3.keys())
output = {}
c = 0

# Association rule generation
for tuples in finalList:
    new_var = []
    for i in range(0, len(finalList[c])):
        new_var.append(finalList[c][i])
    new_var += list(combinations(finalList[c], 2))
    for l in new_var:
        equation = round(
            (((dict3[tuples] / length) / (main_dict[l] / length)) * 100), 2)
        if equation >= min_confidence:
            output[l] = equation
    c += 1

print("\nAssociation rules with confidence greater than or equal to",
      min_confidence, ":")
print(output)