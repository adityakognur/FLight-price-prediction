import pandas as pd
import os
import re

def clean_flight_data(input_file: str, output_file: str):
    df = pd.read_csv(input_file)

    # Example cleaning steps:
    # 1. Remove weird characters from Price, convert to numeric
    df['Price'] = df['Price'].str.replace(r'[^\d.]', '', regex=True)
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    # 2. Convert Duration like '7h 20m' to total minutes as integer
    def duration_to_minutes(duration):
        if pd.isna(duration):
            return None
        hours = re.search(r'(\d+)h', duration)
        minutes = re.search(r'(\d+)m', duration)
        total = 0
        if hours:
            total += int(hours.group(1)) * 60
        if minutes:
            total += int(minutes.group(1))
        return total

    df['Duration_mins'] = df['Duration'].apply(duration_to_minutes)

    # 3. Convert Total stops to numeric (nonstop=0, 1 stop=1, etc.)
    def stops_to_num(stops):
        if pd.isna(stops):
            return None
        if 'nonstop' in stops.lower():
            return 0
        match = re.search(r'(\d+)', stops)
        return int(match.group(1)) if match else None

    df['Total_stops_num'] = df['Total stops'].apply(stops_to_num)

    # 4. Convert Date column to datetime
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')

    # 5. Drop rows with missing critical info (optional)
    df = df.dropna(subset=['Price', 'Duration_mins', 'Total_stops_num', 'Date'])

    # Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved to: {output_file}")

if __name__ == "__main__":
    input_file = os.path.join("..", "data", "processed", "combined_cleaned_data.csv")
    output_file = os.path.join("..", "data", "processed", "cleaned_flight_data.csv")
    clean_flight_data(input_file, output_file)
