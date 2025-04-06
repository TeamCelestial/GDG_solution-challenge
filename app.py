# app.py - Streamlit UI

import streamlit as st
import requests

st.title('AI Moderation System')

# Text input for text prediction
text = st.text_area("Enter text for moderation:")
if st.button('Predict Text'):
    response = requests.post("http://127.0.0.1:8000/predict/text", json={"text": text})
    prediction = response.json()
    st.write(f"Prediction: {prediction['prediction']}")
