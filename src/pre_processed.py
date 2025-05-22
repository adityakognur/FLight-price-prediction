import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle

def preprocess_flight_data(input_file, output_file):
    # Load data
    df = pd.read_csv(input_file)
    
    # 1. Drop missing values
    df.dropna(inplace=True)
    
    # 2. Clean 'Price' column
    df['Price'] = df['Price'].str.replace('SAR', '', regex=False)
    df['Price'] = df['Price'].str.replace(',', '', regex=False)
    df['Price'] = df['Price'].str.strip()
    df['Price'] = df['Price'].astype(float)
    
    # 3. Process 'Total stops'
    df['Total stops'] = df['Total stops'].str.strip()
    df['Total_stops_num'] = df['Total stops'].replace({'nonstop': '0'}).str.extract('(\d+)')
    df['Total_stops_num'] = df['Total_stops_num'].astype(int)
    
    # 4. Convert 'Duration' to minutes
    def duration_to_minutes(duration):
        hours = 0
        minutes = 0
        if 'h' in duration:
            hours = int(duration.split('h')[0])
            if 'm' in duration:
                minutes = int(duration.split('h')[1].replace('m', '').strip())
        else:
            minutes = int(duration.replace('m', '').strip())
        return hours * 60 + minutes
    
    df['Duration_min'] = df['Duration'].apply(duration_to_minutes)
    
    # 5. Process 'Date' column
    # Process 'Date' column with dayfirst=True
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day

    
    # 6. Label encode categorical columns
    le_airline = LabelEncoder()
    le_source = LabelEncoder()
    le_destination = LabelEncoder()
    
    df['Airline_enc'] = le_airline.fit_transform(df['Airline'])
    df['Source_enc'] = le_source.fit_transform(df['Source'])
    df['Destination_enc'] = le_destination.fit_transform(df['Destination'])
    
    # Drop original columns after encoding and processing
    df.drop(['Airline', 'Source', 'Destination', 'Total stops', 'Duration', 'Date'], axis=1, inplace=True)
    
    # Save the processed data to new CSV
    df.to_csv(output_file, index=False)
    
    return df, le_airline, le_source, le_destination

# Example usage:
input_file = '../data/processed/combined_cleaned_data.csv'            # Your input CSV file path
output_file = '../data/processed/processed_flight_data.csv' # Output path for processed data

df_processed, le_airline, le_source, le_destination = preprocess_flight_data(input_file, output_file)


pickle.dump(le_airline, open("../models/le_airline.pkl", "wb"))
pickle.dump(le_source, open("../models/le_source.pkl", "wb"))
pickle.dump(le_destination, open("../models/le_destination.pkl", "wb"))


print("Preprocessing done. Processed data saved to:", output_file)
print(df_processed.head())
