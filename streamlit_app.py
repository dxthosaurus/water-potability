import streamlit as st
import pickle
import numpy as np
import sklearn
import pandas as pd

# Memuat model dari file
with open('models1.pkl', 'rb') as file:
    loaded_models = pickle.load(file)

# Judul aplikasi
st.title("Water Potability Prediction")

# Pilih algoritma
algorithm = st.selectbox("Select Algorithm", options=list(loaded_models.keys()))

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

# Prediksi
if st.button("Predict"):
    features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])

        # Dictionary untuk menampilkan input fitur dengan nama
    feature_names = {
        "Feature": [
            "pH Level",
            "Hardness",
            "Total Dissolved Solids",
            "Chloramines",
            "Sulfate",
            "Conductivity",
            "Organic Carbon",
            "Trihalomethanes",
            "Turbidity"
        ],
        "Value": [
            ph,
            hardness,
            solids,
            chloramines,
            sulfate,
            conductivity,
            organic_carbon,
            trihalomethanes,
            turbidity
        ]
    }

    # Mengonversi dictionary menjadi DataFrame
    feature_df = pd.DataFrame(feature_names)

    # Debugging: Print input features dengan nama
    # Menampilkan tabel input fitur
    st.write("Input Features:")
    st.dataframe(feature_df)  # Atau gunakan st.dataframe(feature_df) untuk interaktivitas lebih
    
    try:
        model = loaded_models[algorithm]
        prediction = model.predict(features)
        if prediction[0] == 1:
            st.success("Water is Potable")
        else:
            st.error("Water is Not Potable")
    except ValueError as e:
        st.error(f"Error during prediction: {e}")
