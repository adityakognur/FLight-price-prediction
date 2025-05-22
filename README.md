# ✈️ Flight Price Prediction

This project predicts the price of a flight ticket based on various input parameters like airline, source, destination, duration, total stops, and date of journey.

## 📁 Project Structure

flight_price_prediction/
│
├── src/ # Source code
│ ├── train_model.py # Model training script
│ ├── predict.py # Test prediction script
│ └── (model is excluded via .gitignore)
│
├── dashboard/
│ └── app.py # Streamlit web interface
│
├── reports/ # Report documents
│ └── duration_vs_prie.png
│
├── models/ # Encoders (Airline, Source, Destination)
│ 
│
├── .gitignore
└── README.md




## 🚀 Features

- Predicts flight prices using a trained machine learning model.
- Takes input via a web interface built with Streamlit.
- Encodes categorical data using pre-fitted `LabelEncoders`.
- Accepts journey date via a calendar input.
- Separates training, prediction, and UI logic.

## 🧠 Model

- The model was trained using:
  - Airline, Source, Destination
  - Number of stops
  - Duration in minutes
  - Journey date (Day, Month, Year)
