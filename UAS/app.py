import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# STAGE 1: Dataset Selection and Exploration
def load_data(file_path):
    data = pd.read_csv('sepatu.csv', delimiter=',', encoding="ISO-8859-1")
    return data

def plot_brand_counts(data):
    brand_counts = data.groupby('Brand_Name').size().sort_values(ascending=False)
    plt.figure(figsize=(10, 8))
    brand_counts.plot(kind='barh', color=sns.color_palette('Dark2', n_colors=len(brand_counts)))
    plt.gca().spines[['top', 'right']].set_visible(False)
    plt.xlabel('Jumlah')
    plt.ylabel('Brand Name')
    plt.title('Jumlah Brand Terjual')
    plt.show()

# STAGE 2: Data Preprocessing
def preprocess_data(data):
    # Add preprocessing steps here (e.g., scaling, encoding)
    pass

# STAGE 3: Model Training
def train_model(X_train, y_train):
    models = {
        'Linear Regression': LinearRegression(),
        'Decision Tree': DecisionTreeRegressor(),
        'SVR': SVR()
    }
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        print(f'{name} model trained.')
    
    return models

# STAGE 4: Model Evaluation
def evaluate_model(models, X_test, y_test):
    for name, model in models.items():
        predictions = model.predict(X_test)
        mae = mean_absolute_error(y_test, predictions)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        print(f'{name} - MAE: {mae}, MSE: {mse}, R2: {r2}')

if __name__ == "__main__":
    # Load data
    data = load_data('sepatu.csv')
    
    # Plot data
    plot_brand_counts(data)
    
    # Preprocess data
    X, y = preprocess_data(data)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train models
    models = train_model(X_train, y_train)
    
    # Evaluate models
    evaluate_model(models, X_test, y_test)
