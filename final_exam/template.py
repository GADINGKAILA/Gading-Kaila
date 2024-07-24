from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Predict', methods=['GET', 'POST'])
def Predict():
    if request.method == 'POST':
        # Add your prediction logic here
        result = "Your prediction result"
        return render_template('result.html', result=result)
    return render_template('Predict.html')

@app.route('/list')
def list_items():
    items = ['Item 1', 'Item 2', 'Item 3']  # Replace with your actual data
    return render_template('list.html', items=items)

@app.route('/data_customer')
def data_customer():
    customers = [
        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}
        # Add more customers as necessary
    ]
    return render_template('data_customer.html', customers=customers)

if __name__ == '__main__':
    app.run(debug=True)
