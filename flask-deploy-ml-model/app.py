from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained machine learning model
model = joblib.load('linear_regression_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict_price():
    prediction_result = None
    if request.method == 'POST':
        # Extract input data from the form
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        sqft_living = int(request.form['sqft_living'])
        sqft_lot = int(request.form['sqft_lot'])
        floors = float(request.form['floors'])
        waterfront = 1 if request.form.get('waterfront') == 'on' else 0
        view = int(request.form['view'])
        condition = int(request.form['condition'])

        # Prepare the input data for prediction
        new_data = [[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition]]

        # Perform prediction
        predicted_price = model.predict(new_data)[0]
        prediction_result = round(predicted_price, 2)

    return render_template('index.html', prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
