import pandas as pd
import math

def Prgm_head() :
    print("\t\t\t====> Welcome in ID3 <======")
    print("\t\tThis program was created by Ken F.M (672020175)\n")
    
    

def copyright() : 
    return '''
    Alright Reserved")
    Copyringht 2023'''
    

def additions() : 
    
    return '''
    The development of this program can help to those who struggle with decision-making,
    like women when faced with choosing food. or choosing the right guy.
    finally i would like to say Thanks a lot to Ms. Christine Dewi Ph.D for all the knowledge, advice and Encouragament..
    Thank for the exitement class in this semester..'''



# Fungsi menghitung entropy dari target colom yang diberikan 
def entropy(target):
    value_counts = target.value_counts()
    entropy_val = 0

    total_samples = len(target)
    for count in value_counts:
        proportion = count / total_samples
        entropy_val -= proportion * math.log2(proportion)

    return entropy_val

#Fungsi Hitung Info Gain untuk feature/node dan kolom target
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


# Node class untuk merepresentasikan decision tree
class Node:
    def __init__(self, feature=None, value=None, results=None):
        self.feature = feature
        self.value = value
        self.results = results
        self.children = {}


#Fungsi Algoritma ID3 untuk membuat decision tree
def id3(data, target_column, features):
    if len(data[target_column].unique()) == 1:
        return Node(results=data[target_column].iloc[0])

    if len(features) == 0:
        # Jika tidak ada features/attribut tersisi, return leaf node dengan hasil mayoritas 
        return Node(results=data[target_column].mode()[0])
        #perhitungan info gain pada setiap atrribut
    info_gains = [(feature, information_gain(data, feature, target_column)) for feature in features]
    best_feature, _ = max(info_gains, key=lambda x: x[1])

    root = Node(feature=best_feature)

    for value in data[best_feature].unique():
        subset = data[data[best_feature] == value]
        if len(subset) == 0:
            # jika subset kosong, masukan nilai mayoritas dari target_column ke node
            root.children[value] = Node(results=data[target_column].mode()[0])
        else:
            # Secara recursif membentuk tree untuk subset
            root.children[value] = id3(subset.drop(columns=[best_feature]), target_column, [f for f in features if f != best_feature])

    return root

# Data sample rekrut karywan 
data = {
    'Karyawan': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Wawancara': ['Baik', 'Cukup', 'Baik', 'Baik', 'Cukup', 'Kurang', 'Kurang', 'Baik', 'Cukup', 'Cukup'],
    'Tes Bakat': ['Baik', 'Kurang', 'Cukup', 'Baik', 'Cukup', 'Cukup', 'Cukup', 'Baik', 'Baik', 'Cukup'],
    'Pengalaman': ['Kurang', 'Kurang', 'Baik', 'Baik', 'Kurang', 'Kurang', 'Kurang', 'Baik', 'Kurang', 'Kurang'],
    'Pendidikan': ['D3', 'S1', 'D3', 'S1', 'D3', 'D3', 'S1', 'D3', 'D3', 'S1'],
    'Hasil': ['Ya', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Ya']
}

df = pd.DataFrame(data)

print("Sampel Data\n");
print("==============================================================================\n")

print(df)

#mengektrasi features(attribut) dan kolom target
target_column = 'Hasil'
features = ['Wawancara', 'Tes Bakat', 'Pengalaman', 'Pendidikan']

# menghitung dan menampilkan nilai parent entropy(kasus sample data karyawab )
print("Gain Information\n");
parent_ent = entropy(df[target_column])
print("Parent Entropy:", parent_ent)

# Menghitung dan print Information Gain untuk setiap feature(attribut)
for feature in features:
    gain = information_gain(df, feature, target_column)
    print(f"Information Gain for {feature}: {gain}")


print("==============================================================================\n")
print("Decision Tree\n");

# Membangun decision tree / splitting the node 
tree = id3(df, target_column, features)

# Fungsi Display decision tree
def print_tree(node, depth=0):
    if node.results is not None:
        print('  ' * depth, f"Result: {node.results}")
    else:
        print('  ' * depth, f"Feature: {node.feature}")
        for value, child_node in node.children.items():
            print('  ' * (depth + 1), f"Value: {value}")
            print_tree(child_node, depth + 2)

# Print decision tree yang terbentuk
print_tree(tree)


print("==============================================================================\n")
while True  :
    Prgm_head()
    # Fungsi untuk traverse atau melintasi decision tree dan mendapatkan hasil berdasarakn inputan user
    def get_decision(tree, features):
        current_node = tree
        while current_node.results is None:
            feature = current_node.feature
            print(f"{feature}:")
            #membuat angka yang diinputkan user merunjuk pada feature
            for idx, value in enumerate(features[feature], start=1):
                print(f"{idx}. {value}")
            user_input = input(f"Berapa Nilai {feature}nya: ")
            #Excection handling...jika user memasukan angka tidak valid pada opsi
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
        

    # Mengumpukan nilai/value attribut yang unik 
    feature_values = {}
    for feature in features:
        feature_values[feature] = df[feature].unique()


    # The Last line Get the result for user input based on the decision tree
    user_result = get_decision(tree, feature_values)
    print(f"\n\nKeputusan : {user_result}\n")

    # Tanya ke user untuk mengulang memasukan input (1 untuk ya 0 untuk tidak)
    user_choice = input("Do you want to check another result? (Enter 1 to continue, 0 to stop): ")
    if user_choice.strip() != '1':

        print(copyright())
        print(additions())
        print("Exiting the program...\n\n")
        break  # Exit the loop if the user enters anything other than 1
  
input("\n\nPress Enter to exit")
