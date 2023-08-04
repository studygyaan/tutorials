import pickle

# Load the model from the .pkl file
with open('linear_regression_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
    
import pandas as pd

# Load the test dataset from CSV or create a DataFrame with the same format
test_data = pd.read_csv('data.csv')  # Replace 'test_data.csv' with the path to your test dataset

# Extract the features from the test data
new_data = [[3, 2, 1500, 4000, 1, 0, 0, 3]]

# Make predictions using the loaded model
predictions = loaded_model.predict(new_data)

# If you want to see the predictions, you can convert the predictions array to a DataFrame
predictions_df = pd.DataFrame(predictions, columns=['predicted_price'])
print(predictions_df)
