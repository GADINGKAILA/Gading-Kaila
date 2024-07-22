import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('sepatu.csv')

# Clean the 'How_Many_Sold' column
data['How_Many_Sold'] = data['How_Many_Sold'].str.replace(',', '').astype(int)

# Create a Streamlit app
st.title('Penjualan Sepatu Berdasarkan Brand')
st.write('Pilih brand untuk melihat produk dengan penjualan tertinggi.')

# Dropdown menu untuk memilih brand
brands = data['Brand_Name'].unique()
selected_brand = st.selectbox('Pilih Brand', brands)

# Filter data untuk brand yang dipilih
brand_data = data[data['Brand_Name'] == selected_brand]

# Find the top-selling product for the selected brand
top_product = brand_data.loc[brand_data['How_Many_Sold'].idxmax()]

# Display the top-selling product details
st.subheader(f'Top-Selling Product for {selected_brand}')
st.write(f"Product Details: {top_product['Product_details']}")
st.write(f"How Many Sold: {top_product['How_Many_Sold']}")
st.write(f"Current Price: {top_product['Current_Price']}")
st.write(f"Rating: {top_product['RATING']}")

# Plot the sales data for the selected brand
fig, ax = plt.subplots()
ax.barh(brand_data['Product_details'], brand_data['How_Many_Sold'], color='skyblue')
ax.set_xlabel('How Many Sold')
ax.set_ylabel('Product Details')
ax.set_title(f'Sales of {selected_brand} Shoes by Product Details')
st.pyplot(fig)
