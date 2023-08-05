import os
import joblib
import numpy as np
from django.shortcuts import render
from .forms import PricePredictionForm

def predict_price(request):
    if request.method == 'POST':
        form = PricePredictionForm(request.POST)
        if form.is_valid():
            # Load the trained linear regression model
            model_path = os.path.join(os.path.dirname(__file__), 'models', 'linear_regression_model.pkl')
            model = joblib.load(model_path)

            # Extract input data from the form
            new_data = np.array(list(form.cleaned_data.values())).reshape(1, -1)

            # Perform prediction
            predicted_price = model.predict(new_data)[0]

            # Prepare the response
            context = {
                'form': form,
                'predicted_price': round(predicted_price, 2),
            }
            return render(request, 'index.html', context)
    else:
        form = PricePredictionForm()

    context = {'form': form}
    return render(request, 'index.html', context)
