import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Assuming your dataset is in a CSV file named 'house_data.csv', you can read it into a pandas DataFrame as follows:
df = pd.read_csv('data.csv')

# Let's take a look at the first few rows of the dataset to understand its structure
print(df.head())

# Now, let's extract the relevant columns from the DataFrame to create our feature matrix X and target variable y.
# 'X' will contain the independent variables (bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition)
# 'y' will contain the target variable (price)

X = df[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition']]
y = df['price']

# Next, you can split the dataset into training and testing sets using sklearn's train_test_split function:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Now, let's specify the feature names for X to avoid the warning message:
feature_names = ['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition']
X_train.columns = feature_names
X_test.columns = feature_names

# Now, you can build your linear regression model using sklearn's LinearRegression class:
model = LinearRegression()

# Fit the model on the training data
model.fit(X_train, y_train)

# Once the model is trained, you can use it to make predictions on new data (test set in this case):
y_pred = model.predict(X_test)

# To evaluate the model's performance, you can use metrics such as Mean Squared Error (MSE) and R-squared:
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# You can also use the trained model to make predictions on new data by providing the feature values:
# For example, to predict the price of a house with 3 bedrooms, 2 bathrooms, 1500 sqft living area, 4000 sqft lot, 1 floor, not waterfront, no view, and condition 3:
new_data = [[3, 2, 1500, 4000, 1, 0, 0, 3]]
predicted_price = model.predict(new_data)
print("Predicted Price:", predicted_price[0])

