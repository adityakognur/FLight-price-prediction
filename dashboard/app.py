import streamlit as st
import pandas as pd
import joblib
import pickle

# Load model and encoders once
@st.cache_resource
def load_model_and_encoders():
    model = joblib.load("../models/flight_price_model.pkl")
    le_airline = pickle.load(open("../models/le_airline.pkl", "rb"))
    le_source = pickle.load(open("../models/le_source.pkl", "rb"))
    le_destination = pickle.load(open("../models/le_destination.pkl", "rb"))
    return model, le_airline, le_source, le_destination

model, le_airline, le_source, le_destination = load_model_and_encoders()

st.title("Flight Price Prediction")

# User inputs
airline = st.selectbox("Airline", le_airline.classes_)
source = st.selectbox("Source City", le_source.classes_)
destination = st.selectbox("Destination City", le_destination.classes_)
total_stops = st.number_input("Total Stops (0 for nonstop)", min_value=0, max_value=3, step=1)
duration_hours = st.number_input("Duration Hours", min_value=0, max_value=24, step=1)
duration_minutes = st.number_input("Duration Minutes", min_value=0, max_value=59, step=1)
# Date picker for journey date
journey_date = st.date_input("Journey Date")

# Extract day, month, year
journey_day = journey_date.day
journey_month = journey_date.month
journey_year = journey_date.year

if st.button("Predict Price"):
    # Encode categorical features
    airline_enc = le_airline.transform([airline])[0]
    source_enc = le_source.transform([source])[0]
    destination_enc = le_destination.transform([destination])[0]

    duration_mins = duration_hours * 60 + duration_minutes

    input_data = {
        'Airline': airline,
        'Source': source,
        'Destination': destination,
        'Total_stops_num': total_stops,
        'Duration_mins': duration_mins,
        'Journey Day': journey_day,
        'Journey Month': journey_month,
        'Journey Year': journey_year
    }

    input_df = pd.DataFrame([input_data])

    predicted_price = model.predict(input_df)[0]
    st.success(f"Predicted Flight Price: {predicted_price:.2f} SAR")
