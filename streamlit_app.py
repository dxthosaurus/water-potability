import streamlit as st
import pickle
import numpy as np

# Memuat model dari file
with open('models.pkl', 'rb') as file:
    loaded_models = pickle.load(file)

# Pilih model yang ingin digunakan
model = loaded_models['Random Forest']  # Ganti dengan model yang diinginkan

# Judul aplikasi
st.title("Water Potability Prediction")

# Input fitur
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, value=7.0)
hardness = st.number_input("Hardness", min_value=0.0, value=100.0)
solids = st.number_input("Total Dissolved Solids", min_value=0, value=1000)
chloramines = st.number_input("Chloramines", min_value=0.0, value=5.0)
sulfate = st.number_input("Sulfate", min_value=0.0, value=200.0)
conductivity = st.number_input("Conductivity", min_value=0.0, value=500.0)
organic_carbon = st.number_input("Organic Carbon", min_value=0.0, value=10.0)
trihalomethanes = st.number_input("Trihalomethanes", min_value=0.0, value=80.0)
turbidity = st.number_input("Turbidity", min_value=0.0, value=4.0)

# Buat prediksi
if st.button("Predict"):
    features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.success("Water is Potable")
    else:
        st.error("Water is Not Potable")
