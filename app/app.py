from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model and feature columns
model = joblib.load('linear_regression_model.pkl')
feature_columns = joblib.load('feature_columns.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Get user input from the form
        data = {
            'Num_Bedrooms': float(request.form['bedrooms']),
            'Num_Bathrooms': float(request.form['bathrooms']),
            'area_scaled': float(request.form['area']),
            'location_souissi': 1 if request.form['location'] == 'Souissi' else 0,
            'type_villa': 1 if request.form['type'] == 'Villa' else 0,
            # Initialize all other location/type columns to 0
            **{col: 0 for col in feature_columns if col not in ['Num_Bedrooms', 'Num_Bathrooms', 'area_scaled', 'location_souissi', 'type_villa']}
        }

        # Create DataFrame
        input_df = pd.DataFrame([data])

        # Ensure column order matches training data
        input_df = input_df[feature_columns]

        # Predict
        predicted_price = model.predict(input_df)[0]
        prediction = f"{predicted_price:,.2f} KMAD"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)