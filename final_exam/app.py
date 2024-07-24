from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Predict', methods=['GET', 'POST'])
def Predict():
    if request.method == 'POST':
        # Extract form data
        data = {
            'Gender': request.form['Gender'],
            'Marital Status': request.form['Marital Status'],
            'Occupation': request.form['Occupation'],
            'Monthly Income': request.form['Monthly Income'],
            'Educational Qualifications': request.form['Educational Qualifications'],
            'Feedback': request.form['Feedback'],
            'Age': request.form['Age'],
            'Family size': request.form['Family size'],
            'latitude': request.form['latitude'],
            'longitude': request.form['longitude'],
            'Pin code': request.form['Pin code']
        }

        # Convert to DataFrame for prediction
        data_df = pd.DataFrame([data])
        
        # Ensure numeric types for certain fields
        data_df['Age'] = pd.to_numeric(data_df['Age'])
        data_df['Family size'] = pd.to_numeric(data_df['Family size'])
        data_df['latitude'] = pd.to_numeric(data_df['latitude'])
        data_df['longitude'] = pd.to_numeric(data_df['longitude'])
        data_df['Pin code'] = pd.to_numeric(data_df['Pin code'])
        
        # Predict using the loaded model
        prediction = model.predict(data_df)[0]
        
        # Render the result template with prediction
        return render_template('result.html', prediction=prediction)
    return render_template('Predict.html')

@app.route('/list')
def list_view():
    # Placeholder for listing items
    return render_template('list.html')

@app.route('/data_customer')
def datacustomer():
    # Placeholder for displaying customer data
    return render_template('data_customer.html')

if __name__ == '__main__':
    app.run(debug=True)
