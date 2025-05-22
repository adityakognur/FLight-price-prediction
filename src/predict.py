import pandas as pd
import joblib
import pickle

# Load model and encoders
model = joblib.load("../models/flight_price_model.pkl")
le_airline = pickle.load(open("../models/le_airline.pkl", "rb"))
le_source = pickle.load(open("../models/le_source.pkl", "rb"))
le_destination = pickle.load(open("../models/le_destination.pkl", "rb"))

# Sample input values
airline = "Air France"
source = "NYC"
destination = "PAR"
total_stops = 0          # nonstop means 0 stops
duration_hours = 7
duration_minutes = 20
journey_day = 1
journey_month = 2
journey_year = 2022


# Encode categorical features
airline_enc = le_airline.transform([airline])[0]
source_enc = le_source.transform([source])[0]
destination_enc = le_destination.transform([destination])[0]

# Calculate total duration in minutes
duration_mins = duration_hours * 60 + duration_minutes

# Prepare dataframe with expected columns
input_data = {
    'Airline': airline,        # e.g. "Air Serbia"
    'Source': source,          # e.g. "PAR"
    'Destination': destination,# e.g. "NYC"
    'Total_stops_num': total_stops,  # integer, e.g. 2
    'Duration_mins': duration_mins,  # integer, e.g. 119
    'Journey Day': journey_day,
    'Journey Month': journey_month,
    'Journey Year': journey_year
}


input_df = pd.DataFrame([input_data])

# Predict price
predicted_price = model.predict(input_df)[0]

print(f"Predicted Flight Price: {predicted_price:.2f} SAR")
