import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("house_price_model.pkl", "rb"))

st.title("House Price Prediction App")

st.write("Enter house details to predict price")

# Example inputs (change based on your dataset features)
area = st.number_input("Area (sq ft)")
bedrooms = st.number_input("Bedrooms", step=1)
bathrooms = st.number_input("Bathrooms", step=1)

if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms]])
    prediction = model.predict(features)
    st.success(f"Predicted Price: {prediction[0]}")
