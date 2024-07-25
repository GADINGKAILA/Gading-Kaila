import streamlit as st
import joblib
import pandas as pd
import os

# Tentukan jalur absolut untuk file model
model_path = os.path.join('C:\\Users\\user\\OneDrive\\Documents\\final_exam - Copy', 'model.pkl')
print(f"Attempting to load model from: {model_path}")

if not os.path.isfile(model_path):
    raise FileNotFoundError(f"Model file {model_path} does not exist.")

model = joblib.load(model_path)

# Streamlit application
def main():
    st.title('Prediction App Marital Status Costumer')

    # Form for input
    with st.form(key='prediction_form'):
        gender = st.selectbox('Gender', ['Male', 'Female','Prefer not to say'])
        occupation = st.selectbox('Occupation', ['Employee', 'Student', 'Self Employed','House wife'])
        monthly_income = st.selectbox('Monthly Income', ['No Income', 'Below Rs.10000', '10001 to 25000', '25001 to 50000', 'More than 50000'])
        educational_qualifications = st.selectbox('Educational Qualifications', ['School','Graduate', 'Post Graduate', 'Ph.D'])
        feedback = st.selectbox('Feedback', ['Positive', 'Negative'])
        age = st.number_input('Age', min_value=0)
        family_size = st.number_input('Family Size', min_value=1, max_value=10)
        latitude = st.number_input('Latitude')
        longitude = st.number_input('Longitude')
        pin_code = st.number_input('Pin Code')

        submit_button = st.form_submit_button(label='Predict')

        if submit_button:
            # Create DataFrame for prediction
            data = pd.DataFrame({
                'Gender': [gender],
                'Occupation': [occupation],
                'Monthly Income': [monthly_income],
                'Educational Qualifications': [educational_qualifications],
                'Feedback': [feedback],
                'Age': [age],
                'Family size': [family_size],
                'latitude': [latitude],
                'longitude': [longitude],
                'Pin code': [pin_code]
            })

            # Predict
            prediction = model.predict(data)[0]
            st.write(f'Prediction Marital Status Customer: {prediction}')

if __name__ == "__main__":
    main()
