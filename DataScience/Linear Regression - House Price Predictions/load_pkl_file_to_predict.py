import pickle

# Load the model from the .pkl file
with open('/kaggle/input/picklefile/linear_regression_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
    
import pandas as pd

# Create a DataFrame with the new data in the same format as the training data
new_data = pd.DataFrame([[3, 2, 1500, 4000, 1, 0, 0, 3]], columns=['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition'])

# Make predictions using the loaded model
predicted_price = loaded_model.predict(new_data)

print("Predicted Price:", predicted_price[0])

