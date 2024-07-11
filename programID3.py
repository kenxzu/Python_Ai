import pandas as pd
import math

# Calculate entropy for a given target column
def entropy(target):
    value_counts = target.value_counts()
    entropy_val = 0

    total_samples = len(target)
    for count in value_counts:
        proportion = count / total_samples
        entropy_val -= proportion * math.log2(proportion)

    return entropy_val

# Calculate information gain for a given feature and target columns
def information_gain(data, feature, target):
    total_entropy = entropy(data[target])

    values = data[feature].unique()
    weighted_entropy = 0

    for value in values:
        subset = data[data[feature] == value]
        weight = len(subset) / len(data)
        weighted_entropy += weight * entropy(subset[target])

    info_gain = total_entropy - weighted_entropy
    return info_gain

# Node class to represent the decision tree
class Node:
    def __init__(self, feature=None, value=None, results=None):
        self.feature = feature
        self.value = value
        self.results = results
        self.children = {}

# ID3 algorithm to build the decision tree
def id3(data, target_column, features):
    if len(data[target_column].unique()) == 1:
        return Node(results=data[target_column].iloc[0])

    if len(features) == 0:
        # If there are no features left, return a leaf node with the majority result
        return Node(results=data[target_column].mode()[0])

    info_gains = [(feature, information_gain(data, feature, target_column)) for feature in features]
    best_feature, _ = max(info_gains, key=lambda x: x[1])

    root = Node(feature=best_feature)

    for value in data[best_feature].unique():
        subset = data[data[best_feature] == value]
        if len(subset) == 0:
            # If subset is empty, assign the majority value of target_column to the node
            root.children[value] = Node(results=data[target_column].mode()[0])
        else:
            # Recursively build the tree for the subset
            root.children[value] = id3(subset.drop(columns=[best_feature]), target_column, [f for f in features if f != best_feature])

    return root

# Data sample
data = {
    'Karyawan': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Wawancara': ['Baik', 'Cukup', 'Baik', 'Baik', 'Cukup', 'Kurang', 'Kurang', 'Baik', 'Cukup', 'Cukup'],
    'Tes Bakat': ['Baik', 'Kurang', 'Cukup', 'Baik', 'Cukup', 'Cukup', 'Cukup', 'Baik', 'Baik', 'Cukup'],
    'Pengalaman': ['Kurang', 'Kurang', 'Baik', 'Baik', 'Kurang', 'Kurang', 'Kurang', 'Baik', 'Kurang', 'Kurang'],
    'Pendidikan': ['D3', 'S1', 'D3', 'S1', 'D3', 'D3', 'S1', 'D3', 'D3', 'S1'],
    'Hasil': ['Ya', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Ya']
}

df = pd.DataFrame(data)
print("Data Sample\n");

print(df)
print("==============================================================================\n")
# Extract features and target column
target_column = 'Hasil'
features = ['Wawancara', 'Tes Bakat', 'Pengalaman', 'Pendidikan']

# Calculate and print Parent Entropy
print("Gain Information\n");
parent_ent = entropy(df[target_column])
print("Parent Entropy:", parent_ent)

# Calculate and print Information Gain for each feature
for feature in features:
    gain = information_gain(df, feature, target_column)
    print(f"Information Gain for {feature}: {gain}")


print("==============================================================================\n")
print("Decision Tree\n");
# Build the decision tree
tree = id3(df, target_column, features)

# Function to print the decision tree
def print_tree(node, depth=0):
    if node.results is not None:
        print('  ' * depth, f"Result: {node.results}")
    else:
        print('  ' * depth, f"Feature: {node.feature}")
        for value, child_node in node.children.items():
            print('  ' * (depth + 1), f"Value: {value}")
            print_tree(child_node, depth + 2)

# Print the constructed decision tree
print_tree(tree)


print("==============================================================================\n")

# Function to traverse the decision tree and get the result for user input
def get_decision(tree, features):
    current_node = tree
    while current_node.results is None:
        feature = current_node.feature
        print(f"Available {feature} values:")
        for idx, value in enumerate(features[feature], start=1):
            print(f"{idx}. {value}")
        user_input = input(f"Enter the number for '{feature}': ")
        try:
            user_idx = int(user_input)
            if user_idx < 1 or user_idx > len(features[feature]):
                print("Invalid input number. Please enter a valid number.")
            else:
                selected_value = features[feature][user_idx - 1]
                current_node = current_node.children[selected_value]
        except ValueError:
            print("Invalid input. Please enter a number.")
    return current_node.results

# Collect unique values for each feature
feature_values = {}
for feature in features:
    feature_values[feature] = df[feature].unique()

# Get the result for user input based on the decision tree
user_result = get_decision(tree, feature_values)
print(f"The final result based on your input: {user_result}\n")


input("Press Enter to exit")
