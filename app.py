import streamlit as st
import pickle
import os

# Load your trained model
# Use a relative path to load the model file from the same directory as app.py
model_path = 'water_potabilitys.sav'  # Adjust this if the file is in a different directory

# Check if the model file exists
if not os.path.isfile(model_path):
    st.error(f"Model file not found: {model_path}")
else:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)

# Function to predict potability
def predict_potability(features):
    return model.predict([features])

# Streamlit app layout
st.title("Water Potability Prediction")

# Input fields for water quality parameters
pH = st.text_input("pH Level", value="7.0")
hardness = st.text_input("Hardness (mg/L)", value="100")
TDS = st.text_input("Total Dissolved Solids (mg/L)", value="300")
chloramines = st.text_input("Chloramines (mg/L)", value="0.5")
sulfate = st.text_input("Sulfate (mg/L)", value="100")
conductivity = st.text_input("Conductivity (µS/cm)", value="500")
organic_carbon = st.text_input("Organic Carbon (mg/L)", value="1.0")
THMs = st.text_input("Trihalomethanes (µg/L)", value="40")
turbidity = st.text_input("Turbidity (NTU)", value="0.5")

# Function to validate and convert input
def convert_to_float(value, default_value=0.0):
    try:
        return float(value)
    except ValueError:
        st.error(f"Invalid input for {value}. Please enter a numeric value.")
        return default_value

# Convert text input to float
features = [
    convert_to_float(pH),
    convert_to_float(hardness),
    convert_to_float(TDS),
    convert_to_float(chloramines),
    convert_to_float(sulfate),
    convert_to_float(conductivity),
    convert_to_float(organic_carbon),
    convert_to_float(THMs),
    convert_to_float(turbidity)
]

# Button to make a prediction
if st.button("Predict Potability"):
    # Check if all features are valid numbers
    if all(isinstance(f, (int, float)) for f in features):
        prediction = predict_potability(features)
        if prediction[0] == 1:
            st.success("Water is Potable")
        else:
            st.error("Water is Not Potable")
    else:
        st.error("Please ensure all fields contain valid numeric values.")

