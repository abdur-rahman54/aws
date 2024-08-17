import joblib
import numpy as np
from sklearn.datasets import load_iris
import warnings
from sklearn.exceptions import InconsistentVersionWarning

def load_model(model_path):
    """
    Load the trained model from the specified file path.
    
    Parameters:
    model_path (str): Path to the model file.
    
    Returns:
    model: The loaded model.
    """
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", InconsistentVersionWarning)
            model = joblib.load(model_path)
        return model
    except Exception as e:
        raise Exception(f"Failed to load model: {e}")

def get_user_input():
    """
    Prompt the user for input and validate it.
    
    Returns:
    np.ndarray: The validated input vector.
    """
    while True:
        user_input = input("Please enter your input (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            return None
        try:
            input_vector = np.array([float(i) for i in user_input.split()])
            if len(input_vector) != 4:
                print("Please enter exactly four numeric values separated by spaces.\n")
            else:
                return input_vector
        except ValueError:
            print("Invalid input format. Please enter numeric values separated by spaces.\n")

def predict_flower(model, input_vector, target_names):
    """
    Use the model to predict the class of the input vector.
    
    Parameters:
    model: The trained model.
    input_vector (np.ndarray): The input vector for prediction.
    target_names (list): List of target class names.
    
    Returns:
    str: The predicted class name.
    """
    try:
        prediction = model.predict([input_vector])
        predicted_class_name = target_names[int(prediction[0])]
        return predicted_class_name
    except Exception as e:
        raise Exception(f"Prediction error: {e}")

def main():
    """
    Main function to run the continuous prediction loop.
    """
    #print("Loading Iris dataset...")
    iris = load_iris()
    target_names = iris['target_names']

    model_path = 'model.pkl'
    #print(f"Loading model from {model_path}...")
    model = load_model(model_path)

    print("Model loaded successfully.")
    print("Input format: sepal_length sepal_width petal_length petal_width\n")

    while True:
        input_vector = get_user_input()
        if input_vector is None:
            print("Exiting the program.")
            break
        try:
            predicted_class_name = predict_flower(model, input_vector, target_names)
            print(f"Predicted flower is '{predicted_class_name}'\n")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
