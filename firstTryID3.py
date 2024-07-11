import math

def calculate_entropy(data):
    # Calculate the entropy of a dataset
    n = len(data)
    if n == 0:
        return 0
    labels = [row[-1] for row in data]
    label_counts = {}
    for label in labels:
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1
    entropy = 0
    for label in label_counts:
        probability = label_counts[label] / n
        entropy -= probability * math.log2(probability)
    return entropy

def calculate_information_gain(data, attribute_index):
    # Calculate the information gain for a specific attribute
    total_entropy = calculate_entropy(data)
    n = len(data)
    attribute_values = set([row[attribute_index] for row in data])
    weighted_entropy = 0
    for value in attribute_values:
        subset = [row for row in data if row[attribute_index] == value]
        weight = len(subset) / n
        weighted_entropy += weight * calculate_entropy(subset)
    information_gain = total_entropy - weighted_entropy
    return information_gain

def split_data(data, attribute_index):
    # Split the data into subsets based on a chosen attribute
    attribute_values = set([row[attribute_index] for row in data])
    subsets = {}
    for value in attribute_values:
        subset = [row for row in data if row[attribute_index] == value]
        subsets[value] = subset
    return subsets

def build_id3_tree(data, attributes):
    # Implement your tree-building logic here
    # Recursive function
    pass

# Example usage:
data = [...]  # Your dataset
attributes = [...]  # List of attribute names

tree = build_id3_tree(data, attributes)
