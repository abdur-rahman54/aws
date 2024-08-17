import pickle
import numpy as np
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Mapping predicted class to actual class label
target_names = iris['target_names']

# Continuous input and prediction loop
while True:
    # Prompt the user for input
    print("input format: sepal_length sepal_width petal_length petal_width\n")
    user_input = input("Please enter your input (or type 'exit' to quit): ")
    
    # Check if the user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break
    
    try:
        # Convert user input into an input vector
        input_vector = np.array([float(i) for i in user_input.split()])
        
        # Use the model to make a prediction
        prediction = model.predict([input_vector])
        
        # Get the predicted class name
        predict_class = int(prediction[0])
        predicted_class_name = target_names[predict_class]
        
        print(f"Predicted flower is '{predicted_class_name}'\n")
    
    except ValueError:
        print("Invalid input format. Please enter numeric values separated by spaces.\n")
    except Exception as e:
        print("An error occurred:", e)

