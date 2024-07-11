import os
import cv2
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

# Load and preprocess the dataset
def load_data():
    data = []
    labels = []
    
    word_path = 'path/to/word_dataset/'
    no_word_path = 'path/to/no_word_dataset/'

    # Load images with words
    for img_name in os.listdir(word_path):
        img_path = os.path.join(word_path, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (64, 64))  # Resize images to a consistent size
        data.append(img)
        labels.append(1)  # Label 1 for images with words

    # Load images without words
    for img_name in os.listdir(no_word_path):
        img_path = os.path.join(no_word_path, img_name)
        img = cv2.imread(img_path)
        img = cv2.resize(img, (64, 64))
        data.append(img)
        labels.append(0)  # Label 0 for images without words

    # Convert lists to numpy arrays
    data = np.array(data)
    labels = np.array(labels)

    # Shuffle the data
    data, labels = shuffle(data, labels, random_state=42)

    return data, labels

# Build the CNN model
def build_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(units=128, activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    return model

# Main function
def main():
    # Load and preprocess data
    data, labels = load_data()

    # Split the data into training and testing sets
    train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.2, random_state=42)

    # Build the model
    model = build_model()

    # Train the model
    model.fit(train_data, train_labels, epochs=10, batch_size=32, validation_split=0.2)

    # Evaluate the model
    accuracy = model.evaluate(test_data, test_labels)
    print(f"Test Accuracy: {accuracy[1]}")

    # Make predictions on new data (replace 'new_images' with your actual data)
    new_images = np.array([...])  # Replace with your new images
    predictions = model.predict(new_images)
    print(predictions)

if __name__ == "__main__":
    main()
